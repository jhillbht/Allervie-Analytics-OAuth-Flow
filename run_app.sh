#!/bin/bash

# Load environment variables
set -a
source .env
set +a

# Start the Flask application
python analytics_web.py