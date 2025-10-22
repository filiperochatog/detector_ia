class RealtimeMonitor:
    def __init__(self, camera, person_detector, helmet_detector):
        self.camera = camera
        self.person_detector = person_detector
        self.helmet_detector = helmet_detector

    def start_monitoring(self):
        while True:
            frame = self.camera.get_frame()
            if frame is None:
                break

            persons = self.person_detector.detect(frame)
            for person in persons:
                helmet_status = self.helmet_detector.detect(frame, person)
                self.draw_results(frame, person, helmet_status)

            self.display_frame(frame)

    def draw_results(self, frame, person, helmet_status):
        # Implement drawing logic here
        pass

    def display_frame(self, frame):
        # Implement frame display logic here
        pass

if __name__ == "__main__":
    from utils.camera import Camera
    from detectors.person_detector import PersonDetector
    from detectors.helmet_detector import HelmetDetector

    camera = Camera()
    person_detector = PersonDetector()
    helmet_detector = HelmetDetector()

    monitor = RealtimeMonitor(camera, person_detector, helmet_detector)
    monitor.start_monitoring()