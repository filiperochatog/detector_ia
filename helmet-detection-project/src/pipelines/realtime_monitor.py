import cv2


class RealtimeMonitor:
    def __init__(self, video_stream, person_detector, helmet_classifier):
        self.video_stream = video_stream
        self.person_detector = person_detector
        self.helmet_classifier = helmet_classifier

    def start(self):
        self.video_stream.open()
        try:
            for frame in self.video_stream.frames():
                annotated = self._process_frame(frame)
                cv2.imshow("Monitoramento EPI", annotated)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            self.video_stream.release()
            cv2.destroyAllWindows()

    def _process_frame(self, frame):
        persons = self.person_detector.detect(frame)
        for person in persons:
            x, y, w, h = person["bbox"]
            has_helmet = self.helmet_classifier.classify(frame, person["bbox"])
            color = (0, 200, 0) if has_helmet else (0, 0, 255)
            label = "Com EPI" if has_helmet else "Sem EPI"
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, max(0, y - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        return frame