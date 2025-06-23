import streamlit as st
import google.generativeai as genai

# === Internal Model Config ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === UI Setup ===
st.set_page_config(page_title="Athlete Training Plan Recommender")
st.title("Athlete Training Plan Recommender")
st.write("This tool uses an adaptive training engine to generate personalized sports training plans based on your current condition and goals.")

# === Input Sliders ===
fitness_level = st.slider("Current Fitness Level", 1, 10, 5)
endurance = st.slider("Endurance / Stamina", 1, 10, 5)
strength = st.slider("Muscle Strength", 1, 10, 5)
recovery = st.slider("Recovery Rate", 1, 10, 6)
training_days = st.slider("Available Training Days per Week", 1, 7, 4)
goal_focus = st.selectbox("Primary Goal", ["Fat Loss", "Muscle Gain", "Endurance", "Strength & Conditioning", "Athletic Performance"])
has_injury = st.selectbox("Any Current Injury?", ["No", "Yes - Minor", "Yes - Significant"])

# === Predict Button ===
if st.button("Generate Training Plan"):
    with st.spinner("Generating adaptive plan..."):
        prompt = f"""
You are a professional-level sports training engine. Based on the athlete's profile, generate:

1. Recommended Training Focus (brief)
2. Weekly Plan Overview (Mon–Sun with rest days)
3. One-line rationale based on stats
4. Avoid casual tone; keep it sports-scientific.

Input Profile:
Fitness Level: {fitness_level}/10  
Endurance: {endurance}/10  
Strength: {strength}/10  
Recovery: {recovery}/10  
Training Days Available: {training_days}  
Primary Goal: {goal_focus}  
Injury Status: {has_injury}

Output format:
Focus: <...>  
Weekly Plan:  
- Mon: ...  
- Tue: ...  
...  
Rationale: <...>
"""

        response = model.generate_content(prompt)
        plan = response.text.strip()

        st.subheader("Your Personalized Training Plan")
        st.text(plan)
