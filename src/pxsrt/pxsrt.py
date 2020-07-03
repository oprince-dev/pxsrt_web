from PIL import Image
import numpy as np
import os


class PxSrt:
    def __init__(self, file):
        self.file = file


    def set_user_choices(self, mode, threshold, direction, reverse, upper):
        self.mode = mode
        self.threshold = threshold
        self.direction = direction
        self.upper = upper
        self.reverse = reverse

    def load_image_data(self):
        ## User won't be able to convert initial image import data between modes unles loads new image
        try:
            with Image.open(self.file) as img:
                # if self.mode in 'HSV':
                #     img = img.convert('HSV')
                self.data = np.asarray(img)
        except FileNotFoundError as e:
            print(e)
            exit()


    def read_thresh(self):
        thresh_data = np.copy(self.data)

        if self.upper:
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
        t_path = 'pxsrt/static/uploads'
        base, ext = os.path.splitext(os.path.basename(self.file))
        t_filename = base + "_thresh" + ext
        if not os.path.exists(t_path):
            os.makedirs(t_path)
        t_filepath = os.path.join(t_path, t_filename)
        if os.path.isfile(t_filepath):
            expand = 0
            while True:
                expand += 1
                expanded_filename = base + "_thresh" + str(expand) + ext
                if os.path.isfile(expanded_filename):
                    continue
                else:
                    t_filename = expanded_filename
                    break
            t_filepath = os.path.join(t_path, t_filename)
            print(t_filepath)
        t_image = Image.fromarray(self.thresh_data, mode='HSV').convert('RGB')
        t_image.save(t_filepath)

        return t_filename
