#!/bin/bash
echo "19th of Nov"
echo "Using gcloud to deploy model to ai-platform"

MODEL_DIR="gs://tutorialwsc2/"
VERSION_NAME="v8"
MODEL_NAME="boston"
FRAMEWORK="SCIKIT_LEARN"

gcloud ai-platform models list
  
gcloud ai-platform versions create $VERSION_NAME \
  --model=$MODEL_NAME \
  --origin=$MODEL_DIR \
  --runtime-version=1.14 \
  --framework=$FRAMEWORK \
  --python-version=3.5 \
  --region=us-central1 \
  --machine-type=n1-standard-4
  
echo "Done"
