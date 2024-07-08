#!/bin/bash

# Define the image name
IMAGE_NAME="kartoza_devops_app2"

# Build the Docker image
docker build -t $IMAGE_NAME .

