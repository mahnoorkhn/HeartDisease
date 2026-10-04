import streamlit as st
import pandas as pd
import pickle


# Load trained model
model = pickle.load(open("heart_model.pkl", "rb"))


# Page title
st.title("Heart Disease Prediction")
st.write("Enter the patient's information below to predict the result.")


# User inputs
age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=55
)

sex = st.selectbox(
    "Sex",
    options=[0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

cp = st.selectbox(
    "Chest Pain Type",
    options=[1, 2, 3, 4]
)

thalach = st.number_input(
    "Maximum Heart Rate",
    min_value=50,
    max_value=250,
    value=150
)


# Prediction button
if st.button("Predict"):

    # Create feature vector
    user_input = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "cp": [cp],
        "thalach": [thalach]
    })

    # Make prediction
    predicted_result = model.predict(user_input)

    # Display result
    if predicted_result[0] == 1:
        st.error("Prediction: HEART DISEASE")
    else:
        st.success("Prediction: NO HEART DISEASE")