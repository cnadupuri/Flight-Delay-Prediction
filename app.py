import streamlit as st
import pandas as pd
import joblib

# ===========================
# Load Models
# ===========================

departure_model = joblib.load("flight_departure_delay_model.pkl")
arrival_model = joblib.load("flight_arrival_delay_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# ===========================
# Page Config
# ===========================

st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Flight Delay Prediction System")
#<<<<<<< HEAD
st.write("Predict both Departure Delay and Arrival Delay using Machine Learning.")
#=======
st.caption("Machine Learning | XGBoost | Streamlit")
st.write("Predict both Departure Delay and Arrival Delay using Machine Learning.")
st.set_page_config(
    page_title="Flight Delay Prediction",
    page_icon="✈️",
    layout="wide"
)
st.sidebar.success("Fill in the flight details below.")
#>>>>>>> 7acd34d (Updated Streamlit UI and flight delay prediction app)

st.sidebar.header("Flight Details")

# ===========================
# Flight Information
# ===========================

from_airport = st.sidebar.selectbox(
    "From Airport",
    ["BOM", "CCU", "DEL"]
)

to_airport = st.sidebar.selectbox(
    "To Airport",
    ["DEL", "HYD"]
)

airline = st.sidebar.selectbox(
    "Airline",
    [
        "Air India",
        "Go Air",
        "Indigo",
        "SpiceJet",
        "Spicejet",
        "Vistara"
    ]
)

category = st.sidebar.selectbox(
    "Flight Category",
    [1, 2, 3, 4]
)

weekday = st.sidebar.selectbox(
    "Weekday",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Saturday",
        "Sunday"
    ]
)

weather = st.sidebar.selectbox(
    "Weather",
    [
        "Cloudy",
        "Heavy rain",
        "Heavy rain at times",
        "Light drizzle",
        "Light rain shower",
        "Mist",
        "Moderate or heavy rain shower",
        "Moderate or heavy rain with thunder",
        "Moderate rain",
        "Moderate rain at times",
        "Overcast",
        "Partly cloudy",
        "Patchy light drizzle",
        "Patchy light rain",
        "Patchy light rain with thunder",
        "Patchy rain possible",
        "Sunny",
        "Thundery outbreaks possible",
        "Torrential rain shower"
    ]
)

st.sidebar.header("Flight Metrics")

distance = st.sidebar.number_input(
    "Distance",
    min_value=0,
    value=1200
)

passenger_load = st.sidebar.number_input(
    "Passenger Load Factor",
    min_value=0.0,
    value=85.0
)

airline_rating = st.sidebar.number_input(
    "Airline Rating",
    value=0.5
)

airport_rating = st.sidebar.number_input(
    "Airport Rating",
    value=0.88
)

market_share = st.sidebar.number_input(
    "Market Share",
    value=5.3
)

otp_index = st.sidebar.number_input(
    "OTP Index",
    value=85.6
)

st.sidebar.header("Weather Details")

wind = st.sidebar.number_input(
    "Wind Speed (Kmph)",
    value=10
)

precip = st.sidebar.number_input(
    "Precipitation (MM)",
    value=0
)

humidity = st.sidebar.number_input(
    "Humidity",
    value=60
)

visibility = st.sidebar.number_input(
    "Visibility",
    value=10
)

pressure = st.sidebar.number_input(
    "Pressure",
    value=1013
)

cloudcover = st.sidebar.number_input(
    "Cloud Cover",
    value=40
)

st.sidebar.header("Date")

year = st.sidebar.number_input(
    "Year",
    value=2020
)

month = st.sidebar.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=1
)

day = st.sidebar.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=15
)

st.sidebar.header("Scheduled Time")

departure_hour = st.sidebar.number_input(
    "Departure Hour",
    min_value=0,
    max_value=23,
    value=8
)

departure_minute = st.sidebar.number_input(
    "Departure Minute",
    min_value=0,
    max_value=59,
    value=30
)

arrival_hour = st.sidebar.number_input(
    "Arrival Hour",
    min_value=0,
    max_value=23,
    value=10
)

arrival_minute = st.sidebar.number_input(
    "Arrival Minute",
    min_value=0,
    max_value=59,
    value=45
)
# ===========================
# Create Input Dictionary
# ===========================

input_data = {
    "Distance": distance,
    "Passenger Load Factor": passenger_load,
    "Airline Rating": airline_rating,
    "Airport Rating": airport_rating,
    "Market Share": market_share,
    "OTP Index": otp_index,
    "weather__hourly__windspeedKmph": wind,
    "weather__hourly__precipMM": precip,
    "weather__hourly__humidity": humidity,
    "weather__hourly__visibility": visibility,
    "weather__hourly__pressure": pressure,
    "weather__hourly__cloudcover": cloudcover,
    "Year": year,
    "Month": month,
    "Day": day,
    "Departure_Hour": departure_hour,
    "Arrival_Hour": arrival_hour,
    "Arrival_Minute": arrival_minute,
    "Departure_Minute": departure_minute
}

# ===========================
# Create DataFrame
# ===========================

input_df = pd.DataFrame([input_data])

# ===========================
# One-Hot Encoding
# ===========================

# From Airport
input_df["From_BOM"] = 1 if from_airport == "BOM" else 0
input_df["From_CCU"] = 1 if from_airport == "CCU" else 0
input_df["From_DEL"] = 1 if from_airport == "DEL" else 0

# To Airport
input_df["To_DEL"] = 1 if to_airport == "DEL" else 0
input_df["To_HYD"] = 1 if to_airport == "HYD" else 0

# Airline
input_df["Airline_Air India"] = 1 if airline == "Air India" else 0
input_df["Airline_Go Air"] = 1 if airline == "Go Air" else 0
input_df["Airline_Indigo"] = 1 if airline == "Indigo" else 0
input_df["Airline_SpiceJet"] = 1 if airline == "SpiceJet" else 0
input_df["Airline_Spicejet"] = 1 if airline == "Spicejet" else 0
input_df["Airline_Vistara"] = 1 if airline == "Vistara" else 0

# Weather
weather_columns = [
    "Cloudy",
    "Heavy rain",
    "Heavy rain at times",
    "Light drizzle",
    "Light rain shower",
    "Mist",
    "Moderate or heavy rain shower",
    "Moderate or heavy rain with thunder",
    "Moderate rain",
    "Moderate rain at times",
    "Overcast",
    "Partly cloudy",
    "Patchy light drizzle",
    "Patchy light rain",
    "Patchy light rain with thunder",
    "Patchy rain possible",
    "Sunny",
    "Thundery outbreaks possible",
    "Torrential rain shower"
]

for w in weather_columns:
    col = f"weather__hourly__weatherDesc__value_{w}"
    input_df[col] = 1 if weather == w else 0

# Category
for i in [1, 2, 3, 4]:
    input_df[f"Category_{i}"] = 1 if category == i else 0

# Weekday
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Saturday",
    "Sunday"
]

for d in weekdays:
    input_df[f"Weekday_{d}"] = 1 if weekday == d else 0

# ===========================
# Match Training Features
# ===========================

input_df = input_df.reindex(columns=feature_names, fill_value=0)
#<<<<<<< HEAD
# ===========================
# Prediction
# ===========================

if st.button("Predict Flight Delay"):

    # Make Predictions
    departure_prediction = departure_model.predict(input_df)[0]
    arrival_prediction = arrival_model.predict(input_df)[0]
#=======
# # ===========================
# Prediction
# ===========================

if st.button("✈️ Predict Flight Delay", key="predict_button", use_container_width=True):

    # Make Predictions
    departure_prediction = round(departure_model.predict(input_df)[0])
    arrival_prediction = round(arrival_model.predict(input_df)[0])
#>>>>>>> 7acd34d (Updated Streamlit UI and flight delay prediction app)

    st.success("Prediction Completed Successfully!")

    st.markdown("---")

    col1, col2 = st.columns(2)

    col1, col2 = st.columns(2)

    with col1:
        
        st.metric(
         label="✈️ Predicted Departure Delay",
         value=f"{departure_prediction:.2f} min"
     )

    with col2:
        st.metric(
           label="🛬 Predicted Arrival Delay",
            value=f"{arrival_prediction:.2f} min"
     )
    st.markdown("---")

#<<<<<<< HEAD
    # Delay Status
    if departure_prediction <= 0:
        st.success("✅ Flight is expected to depart on time.")
    else:
        st.warning(f"⚠️ Expected Departure Delay: {departure_prediction:.2f} minutes")

    if arrival_prediction <= 0:
        st.success("✅ Flight is expected to arrive on time.")
    else:
        st.warning(f"⚠️ Expected Arrival Delay: {arrival_prediction:.2f} minutes")

    st.markdown("---")

    # Show input used for prediction
    with st.expander("View Input Features"):
        st.dataframe(input_df)
      # ===========================
# Prediction
# ===========================

if st.button("Predict Flight Delay"):

    # Make Predictions
    departure_prediction = departure_model.predict(input_df)[0]
    arrival_prediction = arrival_model.predict(input_df)[0]

    st.success("Prediction Completed Successfully!")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="✈️ Predicted Departure Delay",
            value=f"{departure_prediction:.2f} min"
        )

    with col2:
        st.metric(
            label="🛬 Predicted Arrival Delay",
            value=f"{arrival_prediction:.2f} min"
        )

    st.markdown("---")

    # Delay Status
    if departure_prediction <= 0:
        st.success("✅ Flight is expected to depart on time.")
    else:
        st.warning(f"⚠️ Expected Departure Delay: {departure_prediction:.2f} minutes")

    if arrival_prediction <= 0:
        st.success("✅ Flight is expected to arrive on time.")
    else:
        st.warning(f"⚠️ Expected Arrival Delay: {arrival_prediction:.2f} minutes")

    st.markdown("---")

    # Show input used for prediction
    with st.expander("View Input Features"):
        st.dataframe(input_df)
#=======
    # ===========================
    # Departure Status
    # ===========================

    st.subheader("✈️ Departure Status")

    if departure_prediction <= 15:
        st.success(f"🟢 Low Departure Delay: {departure_prediction} minutes")
    elif departure_prediction <= 45:
        st.warning(f"🟡 Moderate Departure Delay: {departure_prediction} minutes")
    else:
        st.error(f"🔴 High Departure Delay: {departure_prediction} minutes")

    # ===========================
    # Arrival Status
    # ===========================

    st.subheader("🛬 Arrival Status")

    if arrival_prediction <= 15:
        st.success(f"🟢 Low Arrival Delay: {arrival_prediction} minutes")
    elif arrival_prediction <= 45:
        st.warning(f"🟡 Moderate Arrival Delay: {arrival_prediction} minutes")
    else:
        st.error(f"🔴 High Arrival Delay: {arrival_prediction} minutes")

    st.markdown("---")

with st.expander("📋 Flight Details"):
    
    st.write(f"**From Airport:** {from_airport}")
    st.write(f"**To Airport:** {to_airport}")
    st.write(f"**Airline:** {airline}")
    st.write(f"**Flight Category:** {category}")
    st.write(f"**Weekday:** {weekday}")
    st.write(f"**Weather:** {weather}")

    st.write("---")

    st.write(f"**Distance:** {distance} km")
    st.write(f"**Passenger Load Factor:** {passenger_load}%")
    st.write(f"**Airline Rating:** {airline_rating}")
    st.write(f"**Airport Rating:** {airport_rating}")
    st.write(f"**Market Share:** {market_share}")
    st.write(f"**OTP Index:** {otp_index}")

    st.write("---")

    st.write(f"**Departure Time:** {departure_hour:02d}:{departure_minute:02d}")
    st.write(f"**Arrival Time:** {arrival_hour:02d}:{arrival_minute:02d}")
    st.write(f"**Date:** {day:02d}/{month:02d}/{year}")
      # ===========================

#>>>>>>> 7acd34d (Updated Streamlit UI and flight delay prediction app)
      # ===========================
# Sidebar Information
# ===========================

st.sidebar.markdown("---")
st.sidebar.header("📌 Project Information")

st.sidebar.info(
    """
**Project:** Flight Delay Prediction

**Algorithms Used:**
- Linear Regression
- Random Forest
- XGBoost (Final Model)

**Framework:**
- Streamlit

**Developer:**
Chaitanya Nadupuri
"""
)

# ===========================
# Main Page Information
# ===========================

st.markdown("---")

st.subheader("📊 About this Project")

st.write("""
This application predicts:

- ✈️ Departure Delay
- 🛬 Arrival Delay

using a Machine Learning model trained on historical flight and weather data.

The model considers:

- Flight Route
- Airline
- Weather Conditions
- Distance
- Passenger Load Factor
- Airline Rating
- Airport Rating
- Market Share
- OTP Index
- Date & Time Features
""")

st.markdown("---")

st.subheader("💡 Tips")

st.info(
"""
✔ Select the correct departure and destination airports.

✔ Enter realistic weather values.

✔ Ratings should match the dataset scale used during training.

✔ The prediction is an estimate based on historical data.
"""
)

st.markdown("---")

st.caption("© 2026 Flight Delay Prediction | Developed using Streamlit & XGBoost")
