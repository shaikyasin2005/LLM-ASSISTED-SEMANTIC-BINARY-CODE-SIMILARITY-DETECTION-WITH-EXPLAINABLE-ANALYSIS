import os
import json
from config import DATASET_PATH, DATASET_INDEX_FILE

def initialize_dataset():

    dataset_pairs = []

    for file in os.listdir(DATASET_PATH):

        if file.endswith(".txt") or file.endswith(".json"):

            file_path = os.path.join(DATASET_PATH, file)

            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)  # since your txt contains valid JSON

                for item in data:

                    conversations = item.get("conversations", [])

                    if len(conversations) >= 2:

                        human_msg = conversations[0].get("value", "")
                        gpt_msg = conversations[1].get("value", "")

                        dataset_pairs.append({
                            "input_prompt": human_msg,
                            "generated_code": gpt_msg
                        })

    with open(DATASET_INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(dataset_pairs, f, indent=4)

    print("Dataset Indexed Successfully ✔")