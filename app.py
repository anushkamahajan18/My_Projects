import streamlit as st
import pickle
import numpy as np

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Delivery Time Predictor", page_icon="🚚", layout="centered")

# -------------------- LOAD MODEL --------------------
model = pickle.load(open("delivery_model.pkl", "rb"))
cols = pickle.load(open("columns.pkl", "rb"))

# -------------------- TITLE --------------------
st.markdown("<h1 style='text-align:center;'>🚚 Delivery Time Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Predict delivery time using Machine Learning</p>", unsafe_allow_html=True)

# -------------------- INPUT SECTION --------------------
st.subheader("📦 Enter Delivery Details")

col1, col2 = st.columns(2)

with col1:
    distance = st.slider("📍 Distance (km)", 1, 50, 5)
    prep_time = st.slider("🍳 Preparation Time (min)", 5, 60, 15)
    experience = st.slider("👨‍💼 Courier Experience (yrs)", 0, 10, 2)

with col2:
    weather = st.selectbox("🌦️ Weather", ["Clear", "Rainy", "Foggy"])
    traffic = st.selectbox("🚦 Traffic Level", ["Low", "Medium", "High"])
    vehicle = st.selectbox("🚗 Vehicle Type", ["Bike", "Car"])
    time_of_day = st.selectbox("🕒 Time of Day", ["Morning", "Afternoon", "Evening", "Night"])

# -------------------- PREDICTION --------------------
if st.button("🚀 Predict Delivery Time"):

    input_data = np.zeros(len(cols))

    for i, col in enumerate(cols):

        if col == "Distance_km":
            input_data[i] = distance

        elif col == "Preparation_Time_min":
            input_data[i] = prep_time

        elif col == "Courier_Experience_yrs":
            input_data[i] = experience

        elif col == f"Weather_{weather}":
            input_data[i] = 1

        elif col == f"Traffic_Level_{traffic}":
            input_data[i] = 1

        elif col == f"Vehicle_Type_{vehicle}":
            input_data[i] = 1

        elif col == f"Time_of_Day_{time_of_day}":
            input_data[i] = 1

    prediction = model.predict([input_data])[0]

    # -------------------- OUTPUT --------------------
    st.markdown("### ⏱️ Estimated Delivery Time")

    st.success(f"""
    🚚 Delivery Time: **{round(prediction, 2)} minutes**
    """)

