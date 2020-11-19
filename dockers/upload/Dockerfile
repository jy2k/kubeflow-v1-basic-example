FROM python:3.7-slim

WORKDIR /app

RUN pip install -U google-cloud-storage

COPY upload.py ./upload.py

ENTRYPOINT [ "python", "upload.py" ]