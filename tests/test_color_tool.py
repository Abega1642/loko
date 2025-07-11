import unittest
import numpy as np

from src.utils.color_tool import ColorRangeDetector


class TestColorRangeDetector(unittest.TestCase):
    def setUp(self):
        self.detector = ColorRangeDetector()

    def test_valid_red(self):
        lb, ub = self.detector.get_range([0, 0, 255])
        self.assertEqual(lb.dtype, np.uint8)
        self.assertEqual(ub.dtype, np.uint8)

    def test_valid_green(self):
        lb, ub = self.detector.get_range([0, 255, 0])
        self.assertEqual(lb.shape, (3,))
        self.assertEqual(ub.shape, (3,))

    def test_valid_blue(self):
        lb, ub = self.detector.get_range([255, 0, 0])
        self.assertTrue(np.all(lb <= ub))

    def test_lower_hue_clipping(self):
        detector = ColorRangeDetector(hue_delta=20)
        lb, ub = detector.get_range([0, 0, 255])
        self.assertGreaterEqual(lb[0], 0)

    def test_upper_hue_clipping(self):
        detector = ColorRangeDetector(hue_delta=200)
        lb, ub = detector.get_range([0, 0, 255])
        self.assertLessEqual(ub[0], 179)

    def test_invalid_color_length(self):
        with self.assertRaises(ValueError):
            self.detector.get_range([255, 0])  # Too short

    def test_invalid_type_string_input(self):
        with self.assertRaises(ValueError):
            self.detector.get_range("red")  # Invalid type

    def test_color_value_out_of_range(self):
        with self.assertRaises(ValueError):
            self.detector.get_range([300, -10, 0])  # Out of bounds

    def test_dtype_and_shape(self):
        lb, ub = self.detector.get_range([123, 50, 220])
        self.assertEqual(lb.shape, (3,))
        self.assertTrue(isinstance(lb[0], np.uint8))

    def test_custom_ranges(self):
        custom = ColorRangeDetector(
            hue_delta=5, saturation_range=(50, 200), value_range=(10, 100)
        )
        lb, ub = custom.get_range([10, 200, 100])
        self.assertEqual(lb[1], 50)
        self.assertEqual(ub[2], 100)


if __name__ == "__main__":
    unittest.main()
