from PIL import Image
import numpy as np
import os
from multiprocessing import Pool



class PxSrt:
    def __init__(self, file):
        self.file = file


    def set_user_choices(self, mode, threshold, direction, upper, reverse):
        self.mode = mode
        self.threshold = int(threshold)
        self.direction = direction
        self.upper = upper
        self.reverse = reverse


    def load_image_data(self):
        try:
            with Image.open("/home/oli/Projects/pxsrt_web/src/" + str(self.file)) as img:
                self.data = np.asarray(img)
        except FileNotFoundError as e:
            print(e)
            exit()

    def save(self, flag):
        t_path = 'src/pxsrt/static/img/thresh'
        s_path = 'src/pxsrt/static/img/sorts'
        if not os.path.exists(t_path):
            os.makedirs(t_path)
        if not os.path.exists(s_path):
            os.makedirs(s_path)

        base, ext = os.path.splitext(os.path.basename(self.file))
        if flag == 'thresh':
            self.t_filename = base + "_thresh" + ext
            t_filepath = os.path.join(t_path, self.t_filename)
            self.t_image.save(t_filepath)
        elif flag == 'sort':
            self.s_filename = base + '_' + str(self.mode) + str(self.direction) + str(self.threshold) + \
                str(self.reverse) + str(self.upper) + ext
            s_filepath = os.path.join(s_path, self.s_filename)
            self.s_image.save(s_filepath)
        else:
            print("flag error")


    def read_thresh(self):
        thresh_data = np.copy(self.data)

        if self.upper == "True":
            thresh_data[thresh_data >= self.threshold] = 255
            thresh_data[thresh_data != 255] = 0
        else:
            thresh_data[thresh_data < self.threshold] = 255
            thresh_data[thresh_data != 255] = 0

        if self.mode == 'H' or 'R':
            thresh_data = np.flip(thresh_data, axis=2)
            thresh_data[:,:,:2] = 0
        elif self.mode == 'S' or 'G':
            thresh_data = np.roll(thresh_data, 1 ,axis=2)
            thresh_data[:,:,:2] = 0
        else:
            thresh_data[:,:,:2] = 0

        self.thresh_data = thresh_data


    def generate_thresh(self):
        self.t_image = Image.fromarray(self.thresh_data, mode='HSV').convert('RGB')
        self.save("thresh")

        return self.t_filename


    def mode_index(self):
        modes = {'H': 0, 'S': 1, 'V':2, 'R': 0, 'G': 1, 'B':2}

        return modes[self.mode]

    def quicksort(self, partition_array, m):
        sorted_partition = partition_array[partition_array[:,m].argsort()]
        if self.reverse == "True":
            sorted_partition = sorted_partition[::-1]

        return sorted_partition


    def partition(self, row, thresh_row):
        m = self.mode_index()
        sorted_row = np.empty((0, 3), np.uint8)
        partition_array = np.empty((0, 3), np.uint8)

        for p, t in zip(row, thresh_row):
            if t[2] == 255:
                partition_array = np.append(partition_array, np.array([p]), axis=0)

            else:
                if len(partition_array) >= 1:
                    sorted_partition = self.quicksort(partition_array, m)
                    sorted_row = np.append(sorted_row, np.array(sorted_partition), axis=0)
                    sorted_row = np.append(sorted_row, np.array([p]), axis=0)
                else:
                    sorted_row = np.append(sorted_row, np.array([p]), axis=0)
                partition_array = np.empty((0, 3), int)

        if len(partition_array) >= 1:
            sorted_partition = self.quicksort(partition_array, m)
            sorted_row = np.append(sorted_row, np.array(sorted_partition), axis=0)

        return sorted_row


    def sort_pixels(self):
        sorted_pixels = []
        for row, thresh_row in zip(self.data, self.thresh_data):
            sorted_row = self.partition(row, thresh_row)
            sorted_pixels.append(sorted_row)

        sorted_pixels = np.asarray(sorted_pixels, dtype=object)
        if self.direction.lower() == 'v':
            sorted_pixels = np.transpose(sorted_pixels, (1,0,2))
        self.s_image = Image.fromarray((sorted_pixels).astype(np.uint8)).convert("RGB")
        self.save("sort")

        return self.s_filename
