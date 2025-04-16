#!/bin/bash
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r backend/requirements.txt

echo "Starting backend..."
# example start, user should replace with actual main file entry point
python backend/scripts/main.py
