class PersonDetector:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)

    def load_model(self, model_path):
        # Load the pre-trained model for person detection
        import cv2
        net = cv2.dnn.readNetFromCaffe(model_path + 'deploy.prototxt', model_path + 'res10_300x300_ssd_iter_140000.caffemodel')
        return net

    def detect_person(self, frame):
        # Prepare the frame for the model
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        self.model.setInput(blob)
        detections = self.model.forward()

        # Loop over the detections
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # Confidence threshold
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                return (startX, startY, endX, endY)

        return None  # No person detected

    def draw_detection(self, frame, box):
        if box is not None:
            (startX, startY, endX, endY) = box
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, "Person Detected", (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame