import os

# Base directory of this project (where config.py lives)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to the trained model and its column/category metadata
MODEL_FILE_PATH = os.path.join(BASE_DIR, "project_app", "Linear_Model.pkl")
JSON_FILE_PATH = os.path.join(BASE_DIR, "project_app", "project_data.json")

# Flask app port
PORT_NUMBER = 5000
