import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(BASE_DIR, "dataset", "raw")
DATASET_INDEX_FILE = os.path.join(BASE_DIR, "dataset", "dataset_index.json")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")