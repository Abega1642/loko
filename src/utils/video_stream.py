import cv2 as cv

class VideoStream:
    def __init__(self, index=0):
        self.cap = cv.VideoCapture(index)

    def read(self):
        ret, frame = self.cap.read()
        if not ret or frame is None:
            raise RuntimeError("Failed to read from camera")
        return frame

    def release(self):
        self.cap.release()