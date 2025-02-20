#!/bin/bash

# Load environment variables
set -a
source .env
set +a

# Create required directories
mkdir -p credentials logs

# Start the application
python run.py