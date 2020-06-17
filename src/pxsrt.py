from PIL import Image
import numpy as np


def main():
    class PxSrt:
        def __init__(self, filepath, mode, threshold, direction, upper, reverse):
            self.filepath = filepath
            self.mode = mode
            self.threshold = threshold
            self.direction = direction
            self.upper = upper
            self.reverse = reverse

    filepath = '../images/tokyo.jpg'
    pxsrt_obj = PxSrt(filepath, 'mode', 'threshold', 'direction', 'upper', 'reverse')


if __name__ == '__main__':
    main()
