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
flowchart TD

subgraph group_serving["Streamlit Serving"]
  node_user(("Flight user<br/>actor"))
  node_app["Streamlit app<br/>Python entry point<br/>[app.py]"]
  node_input["Flight feature input<br/>request data"]
  node_feature_vector["Aligned feature vector<br/>model input"]
  node_predictions["Delay predictions<br/>inference result"]
end

subgraph group_artifacts["Model Artifacts"]
  node_feature_schema["Feature schema<br/>serialized contract<br/>[feature_names.pkl]"]
  node_departure_model["Departure delay model<br/>XGBoost regressor"]
  node_arrival_model["Arrival delay model<br/>XGBoost regressor"]
  node_notebook["Training notebook<br/>offline experimentation"]
end

subgraph group_delivery["Build &amp; Automation"]
  node_requirements["Python dependencies<br/>dependency manifest<br/>[requirements.txt]"]
  node_dockerfile["Container image<br/>Docker build"]
  node_ci{{"GitHub Actions CI/CD<br/>automation workflow<br/>[ci.yml]"}}
end

node_user -->|"uses"| node_app
node_app -->|"collects"| node_input
node_input -->|"prepared as"| node_feature_vector
node_feature_schema -->|"aligns ordering"| node_feature_vector
node_app -->|"loads"| node_feature_schema
node_feature_vector -->|"predicts with"| node_departure_model
node_feature_vector -->|"predicts with"| node_arrival_model
node_departure_model -->|"departure estimate"| node_predictions
node_arrival_model -->|"arrival estimate"| node_predictions
node_predictions -->|"rendered in UI"| node_app
node_notebook -.->|"produces or updates"| node_feature_schema
node_notebook -.->|"trains artifact"| node_departure_model
node_notebook -.->|"requires compatible update"| node_arrival_model
node_requirements -.->|"provides runtime"| node_app
node_dockerfile -->|"packages"| node_app
node_dockerfile -->|"packages"| node_departure_model
node_dockerfile -->|"packages"| node_arrival_model
node_dockerfile -->|"installs"| node_requirements
node_ci -->|"builds or deploys"| node_dockerfile

click node_app "https://github.com/cnadupuri/flight-delay-prediction/blob/main/app.py"
click node_feature_schema "https://github.com/cnadupuri/flight-delay-prediction/blob/main/feature_names.pkl"
click node_departure_model "https://github.com/cnadupuri/flight-delay-prediction/blob/main/flight_departure_delay_model.pkl"
click node_arrival_model "https://github.com/cnadupuri/flight-delay-prediction/blob/main/flight_arrival_delay_model.pkl"
click node_notebook "https://github.com/cnadupuri/flight-delay-prediction/blob/main/airlines%20pred.ipynb"
click node_requirements "https://github.com/cnadupuri/flight-delay-prediction/blob/main/requirements.txt"
click node_dockerfile "https://github.com/cnadupuri/flight-delay-prediction/blob/main/Dockerfile"
click node_ci "https://github.com/cnadupuri/flight-delay-prediction/blob/main/.github/workflows/ci.yml"

classDef toneNeutral fill:#f8fafc,stroke:#334155,stroke-width:1.5px,color:#0f172a
classDef toneBlue fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#172554
classDef toneAmber fill:#fef3c7,stroke:#d97706,stroke-width:1.5px,color:#78350f
classDef toneMint fill:#dcfce7,stroke:#16a34a,stroke-width:1.5px,color:#14532d
classDef toneRose fill:#ffe4e6,stroke:#e11d48,stroke-width:1.5px,color:#881337
classDef toneIndigo fill:#e0e7ff,stroke:#4f46e5,stroke-width:1.5px,color:#312e81
classDef toneTeal fill:#ccfbf1,stroke:#0f766e,stroke-width:1.5px,color:#134e4a
class node_user,node_app,node_input,node_feature_vector,node_predictions toneBlue
class node_feature_schema,node_departure_model,node_arrival_model,node_notebook toneAmber
class node_requirements,node_dockerfile,node_ci toneMint
