import json

def load_quiz():
    with open("backend/data/quiz.json") as f:
        return json.load(f)

def load_careers():
    with open("backend/data/careers.json") as f:
        return json.load(f)

def recommend_career(answers):
    """
    Very simple rule-based engine.
    answers = list of selected options from quiz
    """
    careers = load_careers()

    # Example rule mapping
    if "Math & Science" in answers and "Analytical problem-solving" in answers:
        return careers["AI Engineer"]
    elif "Art & Creativity" in answers:
        return careers["Graphic Designer"]
    elif "Helping people" in answers:
        return careers["Teacher"]
    elif "Business & Economics" in answers:
        return careers["Entrepreneur"]
    else:
        return {"title": "Generalist", "roadmap": ["Explore multiple career paths before specialization"]}