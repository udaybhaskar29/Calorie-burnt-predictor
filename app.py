import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Calorie Predictor")
st.title("Calorie Burn Prediction Application")

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("calorie_burn_prediction_model.pkl")

model = load_model()

# User Input
gender_select = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age (years)", 20, 79, 25)

height = st.slider("Height (cm)", 123, 222, 175)

weight = st.slider("Weight (kg)", 36, 132, 70)

duration = st.slider("Workout Duration (mins)", 1, 30, 15)

heart_rate = st.slider("Heart Rate (BPM)", 67, 128, 100)

body_temp = st.slider("Body Temperature (°C)", 36.0, 42.0, 39.0, 0.1)
# Convert gender to numeric
gender = 1 if gender_select == "Male" else 0

# Prediction
if st.button("Predict Energy Burn"):
    input_data = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }])

    prediction = model.predict(input_data)

    st.success(f"Estimated Calories Burned: {prediction[0]:.2f} kcal")