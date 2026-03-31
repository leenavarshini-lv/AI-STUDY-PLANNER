import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Study Planner Virtual Lab", layout="wide")

menu = st.sidebar.selectbox("Navigation", [
    "Home",
    "Theory",
    "Principle",
    "Study Planner",
    "Quiz",
    "Feedback"
])

# ---------------- HOME ----------------
if menu == "Home":
    st.title("📘 AI Study Planner – Virtual Lab")

    st.subheader("🎯 Objective")
    st.write("""
    To develop an intelligent study planning system that
    allocates study time based on subject priority.
    """)

    st.subheader("🚀 Innovation")
    st.write("""
    ✔ Automatic Time Allocation  
    ✔ Weak Subject Priority Logic  
    ✔ Smart Timetable Generator  
    ✔ Performance Based Suggestions  
    """)

    st.success("This system simulates an AI-based academic planning assistant.")

# ---------------- THEORY ----------------
elif menu == "Theory":
    st.title("📚 Theory")

    st.write("""
    Artificial Intelligence in education helps personalize learning.
    Our system uses a rule-based priority allocation method.

    Priority Score = 100 - Subject Marks

    Higher priority → More allocated time.
    """)

# ---------------- PRINCIPLE ----------------
elif menu == "Principle":
    st.title("⚙ Working Principle")

    st.write("""
    Step 1: User enters subjects  
    Step 2: User enters marks  
    Step 3: System calculates priority  
    Step 4: Study time distributed proportionally  
    Step 5: Timetable generated  
    """)

    st.code("Allocated Time = (Priority / Total Priority) × Total Hours")

# ---------------- STUDY PLANNER ----------------
elif menu == "Study Planner":
    st.title("🗓 Smart Study Planner")

    subjects_input = st.text_input("Enter Subjects (comma separated)")
    total_hours = st.number_input("Enter Total Study Hours Per Day", 1, 12)

    if subjects_input:
        subjects = [s.strip() for s in subjects_input.split(",")]
        scores = []
        priorities = []

        st.subheader("Enter Marks for Each Subject")

        for sub in subjects:
            mark = st.number_input(f"{sub} Marks", 0, 100)
            scores.append(mark)
            priorities.append(100 - mark)

        if st.button("Generate Timetable"):
            total_priority = sum(priorities)

            timetable = []

            for i in range(len(subjects)):
                allocated = (priorities[i] / total_priority) * total_hours
                timetable.append({
                    "Subject": subjects[i],
                    "Allocated Hours": round(allocated, 2)
                })

            df = pd.DataFrame(timetable)

            st.subheader("📌 Generated Study Timetable")
            st.table(df)

            if total_hours > 8:
                st.warning("⚠ Studying more than 8 hours may cause burnout. Take breaks.")

# ---------------- QUIZ ----------------
elif menu == "Quiz":
    st.title("📝 Quick Quiz")

    score = 0

    q1 = st.radio("AI stands for?",
                  ["Artificial Input", "Artificial Intelligence", "Auto Instruction"])

    q2 = st.radio("Priority Score formula?",
                  ["Score + 100", "100 - Score", "Score / 100"])

    if st.button("Submit"):
        if q1 == "Artificial Intelligence":
            score += 1
        if q2 == "100 - Score":
            score += 1

        st.success(f"Your Score: {score}/2")

# ---------------- FEEDBACK ----------------
elif menu == "Feedback":
    st.title("💬 Feedback")

    name = st.text_input("Your Name")
    rating = st.slider("Rate the Virtual Lab", 1, 5)
    comment = st.text_area("Suggestions")

    if st.button("Submit Feedback"):
        data = pd.DataFrame([[name, rating, comment]],
                            columns=["Name", "Rating", "Comment"])

        if os.path.exists("feedback.csv"):
            data.to_csv("feedback.csv", mode='a', header=False, index=False)
        else:
            data.to_csv("feedback.csv", index=False)

        st.success("Thank you for your feedback!")
