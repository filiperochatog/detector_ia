import os
import urllib.request

def download_model(url, save_path):
    if not os.path.exists(save_path):
        print(f"Downloading model from {url}...")
        urllib.request.urlretrieve(url, save_path)
        print(f"Model saved to {save_path}")
    else:
        print(f"Model already exists at {save_path}")

def main():
    models = {
        "helmet_classifier": "http://example.com/path/to/helmet_classifier_model",
        "person_detector": "http://example.com/path/to/person_detector_model"
    }

    for model_name, model_url in models.items():
        save_path = os.path.join("models", f"{model_name}.h5")
        download_model(model_url, save_path)

if __name__ == "__main__":
    main()