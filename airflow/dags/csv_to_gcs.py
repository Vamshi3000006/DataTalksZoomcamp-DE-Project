from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
import requests
import zipfile
import os

from datetime import datetime

# Define Variables
ZIP_FILE_URL = "https://www.dropbox.com/s/cn2utnr5ipathhh/all-the-news-2-1.zip?dl=1"  # Ensure direct download
LOCAL_ZIP_PATH = "/tmp/dataset.zip"
EXTRACTED_CSV_PATH = "/tmp/dataset.csv"
GCS_BUCKET = "bucketforbatch"  # Replace with your GCS bucket name
GCS_OBJECT_NAME = "raw/dataset.csv"  # Path inside GCS

# Function to Download the ZIP File
def download_zip():
    try:
        response = requests.get(ZIP_FILE_URL, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes

        with open(LOCAL_ZIP_PATH, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Download completed: {LOCAL_ZIP_PATH}")
    except Exception as e:
        raise Exception(f"Failed to download file: {str(e)}")

# Function to Extract CSV from ZIP
def extract_csv():
    if not zipfile.is_zipfile(LOCAL_ZIP_PATH):
        raise Exception("Downloaded file is not a valid ZIP archive")

    with zipfile.ZipFile(LOCAL_ZIP_PATH, "r") as zip_ref:
        csv_files = [f for f in zip_ref.namelist() if f.endswith(".csv")]
        if not csv_files:
            raise Exception("No CSV file found in the ZIP archive")

        zip_ref.extract(csv_files[0], "/tmp")
        os.rename(f"/tmp/{csv_files[0]}", EXTRACTED_CSV_PATH)  # Standardize path

    print(f"Extracted CSV saved at: {EXTRACTED_CSV_PATH}")

# Define the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 2, 12),
    "retries": 1,
}

with DAG(
    dag_id="zip_csv_ingestion",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    download_task = PythonOperator(
        task_id="download_zip",
        python_callable=download_zip
    )

    extract_task = PythonOperator(
        task_id="extract_csv",
        python_callable=extract_csv
    )

    upload_task = LocalFilesystemToGCSOperator(
        task_id="upload_to_gcs",
        src=EXTRACTED_CSV_PATH,
        dst=GCS_OBJECT_NAME,
        bucket=GCS_BUCKET,
        mime_type="text/csv"
    )

    # Define Task Dependencies
    download_task >> extract_task >> upload_task
