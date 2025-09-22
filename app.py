import json
from flask import Flask, render_template, request
from backend.quiz_loader import load_quiz, QUIZ_MAP
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
    levels = list(QUIZ_MAP.keys())

    if request.method == "POST":
        # Always get the education level from the form
        education_level = request.form.get("education_level")

        # Check if this POST contains quiz answers
        answered_keys = [
            k for k, v in request.form.items()
            if k.startswith("q") and v.strip() != ""
        ]

        if answered_keys:
            # POST contains answers → process quiz
            quiz = load_quiz(education_level)
            answers = {}

            for q in quiz:
                selected = request.form.get(f"q{q['id']}")
                if not selected:
                    continue
                selected_opt = next(
                    (opt for opt in q["options"] if opt["text"] == selected),
                    None
                )
                if selected_opt:
                    answers[q["id"]] = selected_opt

            # If some answers are missing, reload quiz with error
            if len(answers) < len(quiz):
                return render_template(
                    "index.html",
                    quiz=quiz,
                    education_level=education_level,
                    error="⚠️ Please answer all questions before submitting."
                )

            # All answers valid → calculate scores and show roadmap
            scores = calculate_riasec_score(answers)
            career_roadmap = rule_based_career(scores)
            return render_template("roadmap.html", career=career_roadmap)

        else:
            # POST with only education_level → show quiz once
            quiz = load_quiz(education_level)
            return render_template(
                "index.html",
                quiz=quiz,
                education_level=education_level
            )

    # GET request → show class selection
    return render_template("select_level.html", levels=levels)


if __name__ == "__main__":
    app.run(debug=True)
