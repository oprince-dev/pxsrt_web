from PIL import Image
import numpy as np


def main():
    class PxSrt:
        def __init__(self, filepath, mode,
                    threshold, direction, upper,
                    reverse):
            self.filepath = filepath
            self.mode = mode
            self.threshold = threshold
            self.direction = direction
            self.upper = upper
            self.reverse = reverse

        def load_image_data(self):
            try:
                with Image.open(self.filepath) as img:
                    self.data = np.asarray(img)

            except FileNotFoundError as e:
                print(e)
                exit()

        def display_original_image(self):
            img = Image.fromarray(self.data)
            img.show()

    filepath = '../images/tokyo.jpg'
    pxsrt_obj = PxSrt(
            filepath,
            'mode',
            'threshold',
            'direction',
            'upper',
            'reverse')

    pxsrt_obj.load_image_data()
    print(pxsrt_obj.data)
    pxsrt_obj.display_original_image()


if __name__ == '__main__':
    main()
