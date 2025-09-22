import streamlit as st
from backend.career_engine import load_quiz, recommend_career

st.set_page_config(page_title="Career & Education Advisor", page_icon="🎓")

st.title("🎯 One-Stop Career & Education Advisor")
st.write("Answer a few questions to discover your best career roadmap!")

quiz = load_quiz()
answers = []

for q in quiz:
    choice = st.radio(q["question"], q["options"], key=q["id"])
    answers.append(choice)

if st.button("Get My Career Path"):
    result = recommend_career(answers)
    st.subheader(f"✅ Recommended Career: {result['title']}")
    st.write("### Roadmap")
    for step in result["roadmap"]:
        st.markdown(f"- {step}")