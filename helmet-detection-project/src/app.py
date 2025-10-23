from .utils.video_stream import VideoStream
from .pipelines.realtime_monitor import RealtimeMonitor
from .detectors.person_detector import PersonDetector
from .detectors.helmet_classifier import HelmetClassifier


def main():
    video_stream = VideoStream()
    person_detector = PersonDetector()
    helmet_classifier = HelmetClassifier()
    monitor = RealtimeMonitor(video_stream, person_detector, helmet_classifier)
    monitor.start()


if __name__ == "__main__":
    main()