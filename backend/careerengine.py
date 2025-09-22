from collections import Counter

# Rule-based RIASEC engine
def calculate_riasec_score(answers):
    all_codes = []
    for opt in answers.values():  # answers is dict {q_id: selected_option_dict}
        all_codes.extend(opt.get("code", []))
    return dict(Counter(all_codes))

def generate_career_path(scores):
    # Simple mapping from RIASEC scores to career path
    top_codes = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    primary = top_codes[0][0] if top_codes else None

    # Map to generic stages (can extend later)
    if primary in ["I","R"]:
        stream = "Science Stream"
        degree = "B.Tech / MBBS"
        career = "Engineer / Doctor / Researcher"
        tips = [
            "Focus on Physics, Chemistry, Maths",
            "Choose specialization based on interests",
            "Apply for internships and practical experience",
            "Build your career portfolio and network"
        ]
    elif primary in ["E","C"]:
        stream = "Commerce Stream"
        degree = "B.Com / BBA"
        career = "Manager / Entrepreneur / Analyst"
        tips = [
            "Focus on Accounting, Economics, Business Studies",
            "Choose specialization based on interests",
            "Apply for internships and real projects",
            "Build your career network"
        ]
    elif primary == "A":
        stream = "Arts / Design Stream"
        degree = "B.A / Design / Fine Arts"
        career = "Designer / Artist / Writer"
        tips = [
            "Focus on creative skills and portfolio",
            "Choose specialization based on interests",
            "Participate in competitions and projects",
            "Build a strong portfolio"
        ]
    else:  # S
        stream = "Social Sciences"
        degree = "Psychology / Education / Social Work"
        career = "Teacher / Counselor / Social Worker"
        tips = [
            "Focus on subjects involving people",
            "Choose specialization based on interests",
            "Participate in volunteering or internships",
            "Build experience working with communities"
        ]
    
    roadmap = [
        {"Stage": "10th Class", "Recommendation": stream, "Tip": tips[0]},
        {"Stage": "12th Class", "Recommendation": degree, "Tip": tips[1]},
        {"Stage": "Degree", "Recommendation": degree, "Tip": tips[2]},
        {"Stage": "Job / Masters", "Recommendation": career, "Tip": tips[3]},
    ]
    
    return roadmap
