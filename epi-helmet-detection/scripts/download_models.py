import os
import urllib.request
import zipfile

def download_model(url, model_dir):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    model_zip_path = os.path.join(model_dir, 'model.zip')
    
    print(f"Downloading model from {url}...")
    urllib.request.urlretrieve(url, model_zip_path)
    
    print("Extracting model...")
    with zipfile.ZipFile(model_zip_path, 'r') as zip_ref:
        zip_ref.extractall(model_dir)
    
    os.remove(model_zip_path)
    print("Model downloaded and extracted successfully.")

if __name__ == "__main__":
    model_url = "https://example.com/path/to/your/model.zip"  # Replace with the actual model URL
    model_directory = os.path.join(os.getcwd(), 'models', 'helmet_detection_model')
    
    download_model(model_url, model_directory)