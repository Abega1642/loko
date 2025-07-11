import unittest
import numpy as np
from src.utils.color_range_detector import ColorRangeDetector
from src.utils.color_tracker import ColorTracker


class TestColorTracker(unittest.TestCase):

    def setUp(self):
        self.detector = ColorRangeDetector()
        self.tracker = ColorTracker(self.detector, [0, 255, 255])

    def test_detect_returns_none_for_blank_image(self):
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        bbox = self.tracker.detect_bbox(frame)
        self.assertIsNone(bbox)

    def test_detect_bbox_on_centered_color(self):
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        frame[40:60, 40:60] = [0, 255, 255]
        bbox = self.tracker.detect_bbox(frame)
        self.assertEqual(bbox, (40, 40, 60, 60))

    def test_partial_detection_bbox_shape(self):
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        frame[20:80, 30:90] = [0, 255, 255]
        bbox = self.tracker.detect_bbox(frame)
        self.assertEqual(len(bbox), 4)
        self.assertTrue(all(isinstance(c, int) for c in bbox))

    def test_detection_handles_non_contiguous_memory(self):
        frame = np.zeros((50, 50, 3), dtype=np.uint8)
        frame[10:40, 10:40] = [0, 255, 255]
        frame = np.asfortranarray(frame)
        bbox = self.tracker.detect_bbox(frame)
        self.assertIsNotNone(bbox)

    def test_out_of_bounds_color_raises(self):
        bad_tracker = ColorTracker(self.detector, [300, -1, 999])
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        with self.assertRaises(ValueError):
            bad_tracker.detect_bbox(frame)

    def test_edge_pixel_detection(self):
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        frame[95:99, 95:99] = [0, 255, 255]
        bbox = self.tracker.detect_bbox(frame)
        self.assertTrue(all(0 <= c < 100 for c in bbox))

    def test_multiple_regions_detection(self):
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        frame[10:30, 10:30] = [0, 255, 255]
        frame[70:90, 70:90] = [0, 255, 255]
        bbox = self.tracker.detect_bbox(frame)
        self.assertTrue(bbox[0] <= 10 and bbox[2] >= 90)

    def test_bbox_precision_and_size(self):
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        frame[45:55, 45:55] = [0, 255, 255]
        bbox = self.tracker.detect_bbox(frame)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        self.assertEqual(width, 10)
        self.assertEqual(height, 10)

    def test_detection_on_noisy_background(self):
        frame = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
        frame[30:70, 30:70] = [0, 255, 255]
        bbox = self.tracker.detect_bbox(frame)
        self.assertIsNotNone(bbox)
