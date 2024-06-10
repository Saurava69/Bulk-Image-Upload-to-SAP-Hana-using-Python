import os
from datetime import datetime
from db_setup import connect_to_hana
from image_utils import extract_images_from_zip, read_images
from dotenv import load_dotenv
import uuid

load_dotenv()

def generate_uuid():
    return str(uuid.uuid4())

def insert_img_header(conn, header_id, name, description):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO imgHeaderEntity (id, name, description) VALUES (?, ?, ?)", (header_id, name, description))
    conn.commit()

def insert_images(conn, header_id, images):
    cursor = conn.cursor()
    upload_date = datetime.now()
    for i, (image_name, image_data, width, height, image_format, channels) in enumerate(images):
        image_id = generate_uuid()
        cursor.execute(
            "INSERT INTO imagesEntity (id, header_id, image_name, image_data, width, height, format, channels, upload_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (image_id, header_id, image_name, image_data, width, height, image_format, channels, upload_date)
        )
        print(f"Uploaded {i+1}/{len(images)}: {image_name}")
    conn.commit()

def bulk_upload_images(zip_path, extract_folder, name, description):
    header_id = generate_uuid()
    extract_subfolder = os.path.join(extract_folder, name)
    os.makedirs(extract_subfolder, exist_ok=True)

    extract_images_from_zip(zip_path, extract_subfolder)

    images = read_images(extract_subfolder)

    conn = connect_to_hana()

    insert_img_header(conn, header_id, name, description)
    insert_images(conn, header_id, images)

    conn.close()

if __name__ == "__main__":
    zip_path = input("Enter the path to the zip file: ")
    extract_folder = "extract"
    name = input("Enter the name for the image header: ")
    description = input("Enter the description for the image header: ")

    os.makedirs(extract_folder, exist_ok=True)
    bulk_upload_images(zip_path, extract_folder, name, description)
