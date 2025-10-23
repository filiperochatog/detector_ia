# settings.py

class Settings:
    def __init__(self):
        self.model_paths = {
            'person_detector': 'models/person_detector.h5',
            'helmet_classifier': 'models/helmet_classifier.h5'
        }
        self.detection_threshold = 0.5  # Threshold for detection confidence
        self.video_source = 0  # Default camera source
        self.output_window_name = 'Helmet Detection'
        self.alert_message = 'Atenção: Usuário sem capacete detectado!'