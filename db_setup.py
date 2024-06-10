from hdbcli import dbapi
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_hana():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = int(os.getenv('DB_PORT'))

    conn = dbapi.connect(
        address=host,
        port=port,
        user=user,
        password=password
    )
    return conn

# def create_tables_if_not_exist(conn):
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE imgHeaderEntity (
#         id NVARCHAR(255) PRIMARY KEY,
#         name NVARCHAR(255),
#         description NVARCHAR(1024),
#         upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE  imagesEntity (
#         id NVARCHAR(255) PRIMARY KEY,
#         header_id NVARCHAR(255),
#         image_name NVARCHAR(255),
#         image_data BLOB,
#         image_label NVARCHAR(255),
#         width INT,
#         height INT,
#         format NVARCHAR(50),
#         channels INT,
#         upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         source NVARCHAR(255),
#         FOREIGN KEY (header_id) REFERENCES imgHeaderEntity(id)
#     )
#     """)

#     conn.commit()
