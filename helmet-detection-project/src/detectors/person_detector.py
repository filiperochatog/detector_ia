import cv2


class PersonDetector:
    def __init__(
        self, cascade_path: str | None = None, scale_factor: float = 1.1, min_neighbors: int = 5
    ):
        if cascade_path is None:
            cascade_path = cv2.data.haarcascades + "haarcascade_fullbody.xml"
        self.detector = cv2.CascadeClassifier(cascade_path)
        if self.detector.empty():
            raise RuntimeError("Não foi possível carregar o classificador de pessoas.")
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detections = self.detector.detectMultiScale(
            gray, scaleFactor=self.scale_factor, minNeighbors=self.min_neighbors, minSize=(60, 120)
        )
        persons = [{"bbox": (x, y, w, h)} for (x, y, w, h) in detections]
        return persons