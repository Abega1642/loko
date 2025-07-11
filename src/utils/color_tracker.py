from PIL import Image
import cv2 as cv


class ColorTracker:
    def __init__(self, color_detector, target_bgr):
        self.detector = color_detector
        self.target_bgr = target_bgr

    def detect_bbox(self, frame):
        hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower, upper = self.detector.get_range(self.target_bgr)
        mask = cv.inRange(hsv_img, lower, upper)
        mask_img = Image.fromarray(mask)
        return mask_img.getbbox()
