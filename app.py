import streamlit as st
import google.generativeai as genai

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Streamlit UI Setup ===
st.set_page_config(page_title="🧠 Brain-Age Predictor")
st.title("🧠 Brain-Age Predictor")
st.write("Adjust the sliders based on your current cognitive, behavioral, and lifestyle profile. Gemini will estimate your brain's biological age.")

# === Input Sliders ===
actual_age = st.slider("Your Actual Age", 18, 90, 30)
memory_score = st.slider("Memory Performance", 1, 10, 6)
sleep_hours = st.slider("Average Sleep per Night (hours)", 3, 10, 7)
reaction_time = st.slider("Reaction Time (1 = very slow, 10 = very fast)", 1, 10, 6)
mood_stability = st.slider("Mood Stability", 1, 10, 6)
physical_activity = st.slider("Physical Activity Level", 1, 10, 5)
brain_fog = st.slider("Brain Fog Frequency (1 = often, 10 = never)", 1, 10, 7)

# === Predict Button ===
if st.button("Predict Brain Age"):
    with st.spinner("Analyzing with Gemini..."):
        prompt = f"""
You're a neuroscience model that predicts biological brain age based on cognitive and behavioral indicators.

Use the following profile to estimate:
- Predicted Brain Age (number only)
- Delta vs Actual Age (say whether younger, same, or older)
- 1-line explanation (concise, scientific tone)

Inputs:
Actual Age: {actual_age}
Memory: {memory_score}
Sleep: {sleep_hours} hrs/night
Reaction Time: {reaction_time}/10
Mood Stability: {mood_stability}/10
Physical Activity: {physical_activity}/10
Brain Fog (inverted scale): {brain_fog}/10

Respond in this exact format:
Predicted Brain Age: <age>  
Difference from Actual Age: <Younger | Same | Older>  
Comment: <brief reason>
"""

        response = model.generate_content(prompt)
        result = response.text.strip()

        st.subheader("🧠 Gemini's Prediction")
        st.text(result)
