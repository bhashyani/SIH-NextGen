import json
from flask import Flask, render_template, request, redirect, url_for
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

# Landing page → Intro page
@app.route("/", methods=["GET"])
def home():
    return render_template("intro.html")


# Class selection and quiz route
@app.route("/quiz", methods=["GET", "POST"])
def index():
    levels = list(QUIZ_MAP.keys())

    if request.method == "POST":
        education_level = request.form.get("education_level")

        if not education_level:
            # No level selected yet → show class selection page
            return render_template("select_level.html", levels=levels)

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

            if len(answers) < len(quiz):
                return render_template(
                    "index.html",
                    quiz=quiz,
                    education_level=education_level,
                    error="⚠️ Please answer all questions before submitting."
                )

            scores = calculate_riasec_score(answers)
            career_roadmap = rule_based_career(scores)
            return render_template("roadmap.html", career=career_roadmap)

        else:
            # POST with only education_level → show quiz
            quiz = load_quiz(education_level)
            return render_template(
                "index.html",
                quiz=quiz,
                education_level=education_level
            )

    # GET request → show class selection
    return render_template("select_level.html", levels=levels)


# AI Mentor page with simple interactive form
@app.route("/ai-mentor", methods=["GET", "POST"])
def ai_mentor():
    response = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            # Placeholder AI response
            response = f"🤖 AI Mentor says: I received your question: '{question}'"
    return render_template("ai_mentor.html", response=response)


# ----------------------------
# Sign In / Sign Up Routes
# ----------------------------

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # TODO: Add authentication logic (DB or mock check)
        return redirect(url_for("home"))  # Redirect to intro after login
    return render_template("signin.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        # TODO: Save user details (DB or mock)
        return redirect(url_for("signin"))
    return render_template("signup.html")


# ----------------------------
# Main Entry
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
