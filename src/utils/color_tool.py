import numpy as np
import cv2 as ip


class ColorRangeDetector:
    def __init__(
        self, hue_delta=10, saturation_range=(100, 255), value_range=(100, 255)
    ):
        self.hue_delta = hue_delta
        self.sat_min, self.sat_max = saturation_range
        self.val_min, self.val_max = value_range

    @staticmethod
    def validate_color(color):
        if (
            not isinstance(color, (list, tuple, np.ndarray))
            or len(color) != 3
            or any(c < 0 or c > 255 for c in color)
        ):
            raise ValueError(
                f'Invalid BGR color: {color}. Must be 3 values in range 0–255.'
            )

    def get_range(self, bgr_color):
        self.validate_color(bgr_color)

        hsv_pixel = ip.cvtColor(np.uint8([[bgr_color]]), ip.COLOR_BGR2HSV)[0][0]
        hue = int(hsv_pixel[0])

        lower = np.array(
            [max(hue - self.hue_delta, 0), self.sat_min, self.val_min], dtype=np.uint8
        )

        upper = np.array(
            [min(hue + self.hue_delta, 179), self.sat_max, self.val_max], dtype=np.uint8
        )

        return lower, upper
