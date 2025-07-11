import cv2 as cv


class Visualizer:
    def __init__(self, color=(0, 255, 0), thickness=5):
        self.color = color
        self.thickness = thickness

    def annotate(self, frame, bbox):
        if (
            not bbox
            or not isinstance(bbox, (list, tuple))
            or len(bbox) != 4
            or not all(isinstance(coord, int) for coord in bbox)
        ):
            return frame

        x1, y1, x2, y2 = bbox
        return cv.rectangle(frame, (x1, y1), (x2, y2), self.color, self.thickness)

    def show(self, window_name, frame):
        cv.imshow(window_name, frame)
