from minio import Minio
from minio.error import S3Error

def main():

    # Initialize MinIO client
    client = Minio(
        "localhost:9000",
        access_key="minio",
        secret_key="minio123",
        secure=False
    )

    # The file to upload
    source_file = "./data/upload/test-file.txt"

    bucket = "warehouse-script"
    destination_file = "test-file.txt"

    # Check if bucket exists
    if client.bucket_exists(bucket):
        print(f"{bucket} already exists")
    else:
        print(f"{bucket} does not exist")
        print(f"Creating {bucket} bucket")
        client.make_bucket(bucket)

    # Working with CSV, JSON, and Parquet files (Read/Write)


    # Upload data
    result = client.fput_object(
        bucket,
        destination_file,
        source_file
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket,
    )

    # Download data of an object
    client.fget_object(
        bucket,
        destination_file,
        "./data/downloaded/text-file-downloaded.txt"
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("Error occurred.", exc)