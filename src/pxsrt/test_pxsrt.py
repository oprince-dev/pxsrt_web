import unittest
from unittest import mock
from pxsrt import PxSrt
import numpy as np
import numpy.testing as npt


class TestPxsrt(unittest.TestCase):

    def setUp(self):
        self.pxsrt_obj = PxSrt('pxsrt/static/img/test.jpg')
        self.pxsrt_obj.set_user_choices('H', 200, 'v', True, False)
        self.possible_modes = ['H', 'S', 'V', 'R', 'G', 'B']
        self.possible_directions = ['h', 'v']
        self.pxsrt_obj.load_image_data()
        self.pxsrt_obj.read_thresh()

    def tearDown(self):
        pass

    def test_file(self):
        self.assertEqual(self.pxsrt_obj.file, 'pxsrt/static/img/test.jpg')

    def test_user_choices(self):
        self.assertIn(self.pxsrt_obj.mode, self.possible_modes)
        self.assertEqual(self.pxsrt_obj.threshold, 200)
        self.assertIn(self.pxsrt_obj.direction, self.possible_directions)
        self.assertIs(self.pxsrt_obj.upper, True)
        self.assertIs(self.pxsrt_obj.reverse, False)

    def test_load_image_data(self):
        self.assertIsNotNone(self.pxsrt_obj.data)
        self.assertIs(type(self.pxsrt_obj.data), np.ndarray)
        self.assertGreaterEqual(self.pxsrt_obj.data.shape, (0, 0, 0))

    def test_dtypes(self):
        self.assertEqual(self.pxsrt_obj.data.dtype, 'uint8')
        self.assertEqual(self.pxsrt_obj.thresh_data.dtype, 'uint8')

    def test_thresh_data(self):
        self.assertEqual(self.pxsrt_obj.data.shape,
                         self.pxsrt_obj.thresh_data.shape)
        first_pixel = self.pxsrt_obj.thresh_data[1, 1, :2]
        test_pixel = np.zeros((2,), dtype=np.uint8)
        npt.assert_array_equal(first_pixel, test_pixel)

    @mock.patch('pxsrt.PxSrt.save')
    def test_generate_thresh(self, mock_save):
        self.pxsrt_obj.t_filename = 'test.jpg'
        self.pxsrt_obj.generate_thresh()
        mock_save.assert_called_once_with('thresh')

# load_image_data() requires [file] -> sets [data]
# read_thresh()     requires [data, user choices] -> sets [thresh_data]
# generate_thresh() requires [thresh_data] -> sets [t_image]
# save()            requires [t_image/s_image] -> sets [t_filename, s_filename]
# sort_pixels()     requires [data, thresh_data]
