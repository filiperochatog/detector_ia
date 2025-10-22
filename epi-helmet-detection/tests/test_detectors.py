import unittest
from src.detectors.helmet_detector import HelmetDetector
from src.detectors.person_detector import PersonDetector

class TestDetectors(unittest.TestCase):

    def setUp(self):
        self.helmet_detector = HelmetDetector()
        self.person_detector = PersonDetector()

    def test_helmet_detection(self):
        # Simulate an image with a person wearing a helmet
        image_with_helmet = "path/to/image_with_helmet.jpg"
        result = self.helmet_detector.detect(image_with_helmet)
        self.assertTrue(result, "Helmet detection failed for image with helmet.")

    def test_no_helmet_detection(self):
        # Simulate an image with a person not wearing a helmet
        image_without_helmet = "path/to/image_without_helmet.jpg"
        result = self.helmet_detector.detect(image_without_helmet)
        self.assertFalse(result, "Helmet detection incorrectly identified helmet presence.")

    def test_person_detection(self):
        # Simulate an image with a person
        image_with_person = "path/to/image_with_person.jpg"
        result = self.person_detector.detect(image_with_person)
        self.assertTrue(result, "Person detection failed for image with person.")

    def test_no_person_detection(self):
        # Simulate an image without a person
        image_without_person = "path/to/image_without_person.jpg"
        result = self.person_detector.detect(image_without_person)
        self.assertFalse(result, "Person detection incorrectly identified a person.")

if __name__ == '__main__':
    unittest.main()