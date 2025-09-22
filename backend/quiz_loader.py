import json
import os

# Map education level to quiz file
QUIZ_MAP = {
    "10th Class": "quiz_level1.json",
    "12th Class": "quiz_level2.json",
    "Diploma": "quiz_level3.json",
    "Bachelors": "quiz_level4.json",
    "Masters": "quiz_level5.json"
}

def load_quiz(level: str):
    """
    Loads the quiz JSON file based on the education level.
    """
    quiz_file = QUIZ_MAP.get(level)
    if not quiz_file:
        raise ValueError(f"No quiz file found for level: {level}")

    file_path = os.path.join("backend", "data", quiz_file)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Quiz file {file_path} not found.")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
