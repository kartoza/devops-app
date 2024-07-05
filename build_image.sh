#!/bin/bash

# Define the image name
IMAGE_NAME="kartoza_devops_app"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Print a message indicating the build process is complete
echo "Docker image '$IMAGE_NAME' built successfully."
