import cv2
import numpy as np

class VehicleDetector:

    def __init__(self):
        pass

    def detect_vehicles(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        car_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_car.xml"
        )

        cars = car_cascade.detectMultiScale(gray, 1.1, 2)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return frame, len(cars)