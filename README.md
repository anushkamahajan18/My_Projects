Delivery Time Prediction using Machine Learning

 Project Overview

This project predicts the estimated delivery time (in minutes) based on various real-world factors such as distance, traffic conditions, weather, and courier experience.

It uses a Machine Learning Regression Model and is deployed with a Streamlit web app for interactive predictions.


 Problem Statement

Given delivery-related features, predict how long a delivery will take.


 Features Used

* Distance (km)
* Weather Conditions
* Traffic Level
* Time of Day
* Vehicle Type
* Preparation Time (minutes)
* Courier Experience (years)

Target Variable

* Delivery_Time_min

Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

 Machine Learning Model

* Model Used: Random Forest Regressor
* Evaluation Metrics:

  * R² Score
  * Mean Absolute Error (MAE)

 Project Structure

delivery_project/
│
├── app.py
├── delivery_model.pkl
├── columns.pkl
├── Food_Delivery_Times.csv
└── README.md
App Screenshot

![App Screenshot](images/screenshot.png)

 How to Run the Project

1. Download or Clone Project
git clone <your-repo-link>
cd delivery_project

2. Install Dependencies
pip install pandas numpy scikit-learn streamlit

 3. Run the App
streamlit run app.py

 4. Open in Browser
http://localhost:8501

 Model Performance

* R² Score: (add your value here)
* MAE: (add your value here)

Future Improvements

* Add map-based distance calculation
* Use real-time traffic data
* Deploy on cloud platforms
* Improve UI with charts


