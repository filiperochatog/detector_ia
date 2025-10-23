import cv2

class VideoStream:
    def __init__(self, source: int = 0):
        self.source = source
        self.cap = None

    def open(self):
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            raise RuntimeError("Erro ao abrir a câmera.")

    def frames(self):
        if self.cap is None:
            self.open()
        while True:
            ret, frame = self.cap.read()
            if not ret:
                raise RuntimeError("Erro ao capturar o vídeo.")
            yield frame

    def release(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def start(self, on_frame):
        try:
            for frame in self.frames():
                on_frame(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            self.release()
            cv2.destroyAllWindows()