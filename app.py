import streamlit as st
from backend.quiz_loader import load_quiz

st.title("One-Stop Career & Education Advisor")

# Step 1: Let user choose education level
education_level = st.selectbox(
    "Select your current level:",
    ["10th Class", "12th Class", "Diploma", "Bachelors", "Masters"]
)

# Step 2: Load quiz based on selection
if education_level:
    quiz = load_quiz(education_level)
    st.write(f"### Quiz for {education_level}")

    answers = {}
    for q in quiz:
        st.write(f"**Q{q['id']}: {q['question']}**")
        choice = st.radio(
            f"Choose an option for Q{q['id']}",
            [opt["text"] for opt in q["options"]],
            key=f"q{q['id']}"
        )
        answers[q['id']] = choice

    # Step 3: Submit button
    if st.button("Submit Quiz"):
        st.success("✅ Quiz submitted! (Next: AI career roadmap)")
        st.json(answers)  # temporary check
