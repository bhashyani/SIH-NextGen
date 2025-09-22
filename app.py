import json
from flask import Flask, render_template, request
from backend.quiz_loader import load_quiz
from collections import Counter

app = Flask(__name__)

# Load career JSON
with open("backend/data/careers.json", encoding="utf-8") as f:
    career_data = json.load(f)

def calculate_riasec_score(answers):
    all_codes = []
    for opt in answers.values():
        all_codes.extend(opt.get("code", []))
    return dict(Counter(all_codes))

def rule_based_career(scores):
    # Determine top RIASEC code
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_codes = [c for c, s in sorted_scores if s == sorted_scores[0][1]]

    # Map top RIASEC to career
    if "I" in top_codes or "R" in top_codes:
        career_key = "AI Engineer"
    elif "A" in top_codes:
        career_key = "Graphic Designer"
    elif "E" in top_codes or "S" in top_codes:
        career_key = "Entrepreneur"
    else:
        career_key = "Teacher"

    return career_data[career_key]  # Return full JSON object

# ----------------------------
# Routes
# ----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    print("Req recieved")
    education_level = request.form.get("education_level", "10th Class")
    quiz = load_quiz(education_level)
    print("Quiz Loaded:",quiz)

    if request.method == "POST":
        print("Processing POST req")
        answers = {}
        for q in quiz:
            selected = request.form.get(f"q{q['id']}")
            selected_opt = next(opt for opt in q["options"] if opt["text"] == selected)
            answers[q['id']] = selected_opt

        scores = calculate_riasec_score(answers)
        print("Scores:",scores)
        career_roadmap = rule_based_career(scores)
        print("Career Roadmap:",career_roadmap)
        return render_template("roadmap.html", career=career_roadmap)

    return render_template("index.html", quiz=quiz)

if __name__ == "__main__":
    app.run(debug=True)
