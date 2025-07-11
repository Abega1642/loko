import cv2 as cv
from PIL import Image

from src.utils.color_tool import ColorRangeDetector

cap = cv.VideoCapture(0)
yellow = [0, 255, 255]
green = (0, 255, 0)
color_ranger_detector = ColorRangeDetector()
while True:
    ret, frame = cap.read()

    hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_bound, upper_bound = color_ranger_detector.get_range(yellow)

    mask = cv.inRange(hsv_img, lower_bound, upper_bound)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x_1, y_1, x_2, y_2 = bbox
        frame = cv.rectangle(frame, (x_1, y_1), (x_2, y_2), green, 5)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()