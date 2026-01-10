import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Member A – Study Techniques & Effectiveness",
    layout="wide"
)

# -------------------------------------------------
# Title & Objective
# -------------------------------------------------
st.title("Member A: Study Techniques & Learning Effectiveness")

st.markdown("""
### Objective  
To analyze the **frequency of study techniques used by students** and to examine their **perceived effectiveness** based on survey responses.

This analysis helps identify which study strategies are commonly practiced and which are considered most effective by students.
""")

st.markdown("---")

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

df = load_data()

# -------------------------------------------------
# 1️⃣ Frequency of Study Techniques
# -------------------------------------------------
st.subheader("1️⃣ Average Frequency of Study Techniques")

freq_cols = [
    "freq_reading", "freq_videos", "freq_practice",
    "freq_group", "freq_summary", "freq_flashcards", "freq_teaching"
]

freq_means = df[freq_cols].mean().reset_index()
freq_means.columns = ["Study Technique", "Average Frequency"]

fig1 = px.bar(
    freq_means,
    x="Study Technique",
    y="Average Frequency",
    title="Average Frequency of Study Techniques Used",
    text_auto=True,
    color="Average Frequency",
    color_continuous_scale="Blues"
)

fig1.update_layout(yaxis_title="Frequency Score (1–5)", xaxis_title="")

st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
**Insight:**  
Students most frequently use **reading notes, watching videos, and doing practice exercises**, while techniques such as **teaching others** and **flashcards** are used less often.
""")

# -------------------------------------------------
# 2️⃣ Perceived Effectiveness of Study Techniques
# -------------------------------------------------
st.subheader("2️⃣ Perceived Effectiveness of Study Techniques")

eff_cols = [
    "eff_reading", "eff_practice", "eff_group",
    "eff_flashcards", "eff_videos"
]

eff_means = df[eff_cols].mean().reset_index()
eff_means.columns = ["Study Technique", "Perceived Effectiveness"]

fig2 = px.bar(
    eff_means,
    x="Study Technique",
    y="Perceived Effectiveness",
    title="Perceived Effectiveness of Study Techniques",
    text_auto=True,
    color="Perceived Effectiveness",
    color_continuous_scale="Greens"
)

fig2.update_layout(yaxis_title="Effectiveness Score (1–5)", xaxis_title="")

st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
**Insight:**  
**Practice-based techniques** and **group study** receive higher effectiveness ratings, suggesting that **active learning strategies** are more beneficial than passive ones.
""")

# -------------------------------------------------
# 3️⃣ Frequency vs Effectiveness Comparison
# -------------------------------------------------
st.subheader("3️⃣ Frequency vs Effectiveness of Study Techniques")

comparison = freq_means.merge(eff_means, on="Study Technique")

fig3 = px.scatter(
    comparison,
    x="Average Frequency",
    y="Perceived Effectiveness",
    text="Study Technique",
    size="Perceived Effectiveness",
    color="Perceived Effectiveness",
    title="Comparison Between Frequency and Effectiveness"
)

fig3.update_traces(textposition="top center")

st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
**Insight:**  
Some study techniques are **frequently used but not highly effective**, indicating a gap between students’ habits and optimal learning strategies.
""")

# -------------------------------------------------
# 4️⃣ Study Preference: Alone vs Group
# -------------------------------------------------
st.subheader("4️⃣ Study Preference: Alone vs With Others")

pref_counts = df["study_preference"].value_counts().reset_index()
pref_counts.columns = ["Study Preference", "Count"]

fig4 = px.pie(
    pref_counts,
    names="Study Preference",
    values="Count",
    title="Study Preference Distribution",
    hole=0.4
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
**Insight:**  
Students show mixed preferences between studying **alone** and **with others**, highlighting the importance of flexible learning environments.
""")

# -------------------------------------------------
# 5️⃣ Preferred Study Time
# -------------------------------------------------
st.subheader("5️⃣ Preferred Study Time")

time_counts = df["study_time"].value_counts().reset_index()
time_counts.columns = ["Study Time", "Number of Students"]

fig5 = px.bar(
    time_counts,
    x="Study Time",
    y="Number of Students",
    title="Preferred Study Time Among Students",
    text_auto=True,
    color="Number of Students"
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
**Insight:**  
Most students prefer studying during specific periods of the day, indicating that **study timing** may influence learning effectiveness.
""")

# -------------------------------------------------
# Conclusion
# -------------------------------------------------
st.markdown("---")
st.subheader("Conclusion (Member A)")

st.markdown("""
The findings show that while students use a wide range of study techniques, **frequently used methods are not always the most effective**.  
Active learning strategies such as **practice exercises and group discussions** tend to provide higher perceived benefits.

These insights emphasize the need to guide students toward **more effective study practices**, rather than relying solely on familiar habits.
""")
