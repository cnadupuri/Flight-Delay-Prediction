# ✈️ Flight Delay Prediction using Machine Learning

## 📌 Project Overview

This project predicts:

- Departure Delay
- Arrival Delay

using Machine Learning (XGBoost Regressor).

The application is built with Streamlit and follows an end-to-end MLOps workflow including Docker, GitHub Actions (CI/CD), and cloud deployment.

---

## 📂 Dataset Features

- From
- To
- Airline
- Distance
- Passenger Load Factor
- Airline Rating
- Airport Rating
- Market Share
- OTP Index
- Weather Conditions
- Date Features
- Scheduled Departure Time
- Scheduled Arrival Time

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Streamlit
- Joblib
- Docker
- GitHub Actions

---

## 🤖 Models Used

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

Final Model:
- XGBoost Regressor

---

## 📊 Evaluation Metrics

- MAE
- RMSE
- R² Score

---

## 🚀 Run the Project

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Flight-Delay-Prediction/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── feature_names.pkl
├── flight_departure_delay_model.pkl
├── flight_arrival_delay_model.pkl
└── airlines pred.ipynb
```
