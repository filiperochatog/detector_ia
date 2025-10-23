import cv2
import numpy as np


class HelmetClassifier:
    def __init__(self, coverage_threshold: float = 0.08):
        self.coverage_threshold = coverage_threshold

    def classify(self, frame, bbox):
        x, y, w, h = bbox
        head_height = max(int(h * 0.4), 1)
        head_region = frame[y : y + head_height, x : x + w]
        if head_region.size == 0:
            return False

        hsv = cv2.cvtColor(head_region, cv2.COLOR_BGR2HSV)

        yellow_mask = cv2.inRange(hsv, (20, 100, 100), (35, 255, 255))
        orange_mask = cv2.inRange(hsv, (5, 100, 100), (20, 255, 255))
        white_mask = cv2.inRange(hsv, (0, 0, 200), (180, 40, 255))

        helmet_mask = cv2.bitwise_or(cv2.bitwise_or(yellow_mask, orange_mask), white_mask)
        coverage = float(np.count_nonzero(helmet_mask)) / helmet_mask.size
        return coverage >= self.coverage_threshold