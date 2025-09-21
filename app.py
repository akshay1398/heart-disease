import numpy as np 
import streamlit as st
import pickle

with open('model.pkl','rb') as f:
    final_model = pickle.load(f)




age = st.number_input("Age", min_value=1, max_value=120, step=1)
sex = st.selectbox("Sex", [0, 1])  # 0 = female, 1 = male
cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, step=1)
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.number_input("Resting ECG Results (0-2)", min_value=0, max_value=2, step=1)
thalach = st.number_input("Max Heart Rate Achieved")
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression")
slope = st.number_input("Slope of Peak Exercise ST Segment (0-2)", min_value=0, max_value=2, step=1)
ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, step=1)
thal = st.number_input("Thal (0=Normal, 1=Fixed defect, 2=Reversible defect)", min_value=0, max_value=2, step=1)



input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

if st.button('predict'):
    input_array = np.asarray(input_data, dtype=float).reshape(1, -1)
    result = final_model.predict(input_array)

    if result == 1:
        st.error("⚠️ Defective Heart")
    else:
        st.success("💚 Healthy Heart")