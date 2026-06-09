import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="JARVIS Grade Calculator",
    page_icon="🤖",
    layout="wide"
)

# Iron Man Theme CSS
st.markdown("""
<style>

body {
    background-color: #0a0f1f;
}

.main {
    background-color: #0a0f1f;
}

h1 {
    color: #00ffff;
    text-align: center;
}

.jarvis-box {
    border: 2px solid cyan;
    padding: 20px;
    border-radius: 15px;
    background-color: rgba(0,255,255,0.05);
    box-shadow: 0px 0px 20px cyan;
}

.result {
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    color: cyan;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 JARVIS Grade Calculator")

st.markdown("""
<div class='jarvis-box'>
Enter student marks and JARVIS will calculate the grade.
</div>
""", unsafe_allow_html=True)

# Input
marks = st.number_input(
    "Enter Marks",
    min_value=-10,
    max_value=110,
    step=1
)

# Button
if st.button("Calculate Grade"):

    if marks > 100 or marks < 0:
        grade = "Invalid Input ❌"

    elif marks >= 90:
        grade = "Grade A 🏆"

    elif marks >= 80:
        grade = "Grade B 🥇"

    elif marks >= 70:
        grade = "Grade C 🥈"

    elif marks >= 60:
        grade = "Grade D 🥉"

    elif marks >= 40:
        grade = "Grade E ✔️"

    else:
        grade = "Fail ❌"

    st.markdown(
        f"<div class='result'>{grade}</div>",
        unsafe_allow_html=True
    )
