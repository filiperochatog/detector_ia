# Contents of /epi-helmet-detection/epi-helmet-detection/src/config/settings.py

class Settings:
    def __init__(self):
        self.camera_index = 0  # Index of the camera to use
        self.confidence_threshold = 0.5  # Confidence threshold for detection
        self.helmet_detection_model_path = "models/helmet_detection_model.h5"  # Path to the helmet detection model
        self.person_detection_model_path = "models/person_detection_model.h5"  # Path to the person detection model
        self.video_output_path = "output/video_output.avi"  # Path to save the output video
        self.log_file_path = "logs/detection.log"  # Path for the log file

    def display_settings(self):
        print("Camera Index:", self.camera_index)
        print("Confidence Threshold:", self.confidence_threshold)
        print("Helmet Detection Model Path:", self.helmet_detection_model_path)
        print("Person Detection Model Path:", self.person_detection_model_path)
        print("Video Output Path:", self.video_output_path)
        print("Log File Path:", self.log_file_path)

settings = Settings()