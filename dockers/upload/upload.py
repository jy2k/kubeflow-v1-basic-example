from google.cloud import storage
import argparse

def upload_blob(model):

    bucket_name = "tutorialwsc"
    source_file_name = model
    destination_blob_name = "model.pkl"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    print("bucket: " + str(bucket))
    blob = bucket.blob(destination_blob_name)
    print("blob: " + str(blob))
    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    args = parser.parse_args()
    upload_blob(args.model)