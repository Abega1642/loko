import unittest
import numpy as np

from src.utils.visualizer import Visualizer


class TestVisualizer(unittest.TestCase):

    def setUp(self):
        self.visualizer = Visualizer(color=(0, 255, 0), thickness=3)

    def test_annotate_with_bbox_changes_image(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        bbox = (10, 10, 50, 50)
        annotated = self.visualizer.annotate(img.copy(), bbox)
        self.assertFalse(np.array_equal(annotated, img))

    def test_annotate_with_none_bbox_returns_original(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        annotated = self.visualizer.annotate(img.copy(), None)
        self.assertTrue(np.array_equal(annotated, img))

    def test_bbox_boundaries_respected(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        bbox = (10, 10, 90, 90)
        annotated = self.visualizer.annotate(img.copy(), bbox)
        self.assertEqual(annotated.shape, img.shape)

    def test_color_thickness_applied_correctly(self):
        vis = Visualizer(color=(255, 0, 0), thickness=5)
        img = np.zeros((60, 60, 3), dtype=np.uint8)
        annotated = vis.annotate(img.copy(), (5, 5, 50, 50))
        self.assertFalse(np.array_equal(annotated, img))

    def test_different_color_annotation(self):
        vis1 = Visualizer(color=(0, 255, 0))
        vis2 = Visualizer(color=(0, 0, 255))
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        result1 = vis1.annotate(img.copy(), (20, 20, 80, 80))
        result2 = vis2.annotate(img.copy(), (20, 20, 80, 80))
        self.assertFalse(np.array_equal(result1, result2))

    def test_overlapping_annotations(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        result = self.visualizer.annotate(img.copy(), (10, 10, 40, 40))
        result = self.visualizer.annotate(result, (30, 30, 70, 70))
        self.assertEqual(result.shape, img.shape)

    def test_invalid_bbox_gracefully_handled(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        bad_bbox = ('a', None, 3.14, [5])
        try:
            self.visualizer.annotate(img.copy(), bad_bbox)
        except Exception as e:
            self.fail(f"annotate() raised an unexpected exception: {e}")

    def test_custom_thickness_applied(self):
        vis = Visualizer(color=(255, 255, 0), thickness=7)
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        annotated = vis.annotate(img.copy(), (10, 10, 80, 80))
        self.assertEqual(annotated.shape, img.shape)

    def test_zero_thickness_does_not_crash(self):
        vis = Visualizer(color=(255, 0, 255), thickness=0)
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        try:
            annotated = vis.annotate(img.copy(), (5, 5, 95, 95))
            self.assertTrue(annotated is not None)
        except Exception as e:
            self.fail(f"annotate() with zero thickness raised: {e}")
