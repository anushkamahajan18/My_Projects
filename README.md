
### Delivery Time Predictor

A Machine Learning Web Application for Predicting Delivery Time

Python Streamlit Machine Learning

### Live Demo

(https://myprojects-kpfyr42gn7vqxmuss8bc9n.streamlit.app/)

### Overview

The Delivery Time Predictor is an end-to-end machine learning project designed to estimate delivery time based on real-world factors such as distance, traffic, weather, and courier experience.

The project covers the complete pipeline, including data preprocessing, feature engineering, model training, and deployment using a Streamlit-based web application.

Objective: To help estimate accurate delivery times for better logistics planning and user expectations

### Key Features

* Predicts delivery time based on real-world conditions
* Uses features like distance, traffic, weather, and courier experience
* Interactive and user-friendly web interface built with Streamlit
* Trained on structured delivery dataset
* Ready-to-use serialized machine learning model for deployment

### Project Structure

```
Delivery_Time_Prediction/
├── Delivery.ipynb          # Data analysis and model training
├── app.py                  # Streamlit application
├── delivery_model.pkl      # Trained model
├── columns.pkl             # Feature columns
├── Food_Delivery_Times.xls # Dataset
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

### Dataset

The dataset contains delivery-related information with the following attributes:

* Distance_km
* Weather
* Traffic_Level
* Time_of_Day
* Vehicle_Type
* Preparation_Time_min
* Courier_Experience_yrs
* Delivery_Time_min (Target variable)

### Feature Engineering

The dataset was preprocessed using the following steps:

* Handled missing values
* Removed unnecessary columns like Order_ID
* Converted categorical variables using one-hot encoding
* Prepared features and target variable for model training

### Model Development

Multiple models can be used, but the final selected model is:

### Random Forest Regressor

* n_estimators = 200
* max_depth = 20
* random_state = 42

### Evaluation Metrics:

* R² Score
* Mean Absolute Error (MAE)

### Web Application

The Streamlit application allows users to input delivery details and get instant predictions.

 Inputs

* Distance (km)
* Weather
* Traffic Level
* Time of Day
* Vehicle Type
* Preparation Time (minutes)
* Courier Experience (years)

### Output

* Predicted Delivery Time (minutes)


### Prerequisites

* Python 3.8 or above

### Installation

pip install -r requirements.txt
```

###  Run the Application

```
streamlit run app.py
```

---

### Note

Ensure that the following files are present in the same directory as `app.py`:

* delivery_model.pkl
* columns.pkl

---

## Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit
* Jupyter Notebook

---

## Author

Your Name- Anushka Mahajan

---

## Notes

This project demonstrates a real-world regression use case using machine learning and an interactive web interface.

