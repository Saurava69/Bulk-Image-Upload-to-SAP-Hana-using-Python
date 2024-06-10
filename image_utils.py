import os
import zipfile
from PIL import Image

def extract_images_from_zip(zip_path, extract_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

def read_images(image_folder):
    images = []
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(image_folder, filename)
            with open(file_path, "rb") as image_file:
                encoded_image = image_file.read()
            with Image.open(file_path) as img:
                width, height = img.size
                image_format = img.format
                channels = len(img.getbands())
            images.append((filename, encoded_image, width, height, image_format, channels))
    return images
