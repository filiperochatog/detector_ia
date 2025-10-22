# File: /epi-helmet-detection/epi-helmet-detection/src/main.py

import cv2
from detectors.helmet_detector import HelmetDetector
from detectors.person_detector import PersonDetector
from pipelines.realtime_monitor import RealtimeMonitor

def main():
    # Initialize the detectors
    person_detector = PersonDetector()
    helmet_detector = HelmetDetector()

    # Start the real-time monitoring pipeline
    monitor = RealtimeMonitor(person_detector, helmet_detector)
    monitor.start()

if __name__ == "__main__":
    main()