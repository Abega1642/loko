import cv2 as cv

from src.utils.color_range_detector import ColorRangeDetector
from src.utils.color_tracker import ColorTracker
from src.utils.video_stream import VideoStream
from src.utils.visualizer import Visualizer


class ColorTrackingApp:
    def __init__(self, bgr_color, cam_index=0):
        self.stream = VideoStream(index=cam_index)
        self.tracker = ColorTracker(ColorRangeDetector(), bgr_color)
        self.visualizer = Visualizer()

    def run(self):
        try:
            while True:
                frame = self.stream.read()
                bbox = self.tracker.detect_bbox(frame)
                frame = self.visualizer.annotate(frame, bbox)
                self.visualizer.show("Tracking", frame)

                if cv.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            self.stream.release()
            cv.destroyAllWindows()
