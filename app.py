import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Flight Delay Prediction System",
    page_icon="✈️",
    layout="wide"
)

# ============================================
# LOAD MODELS
# ============================================

@st.cache_resource
def load_models():
    departure_model = joblib.load("flight_departure_delay_model.pkl")
    arrival_model = joblib.load("flight_arrival_delay_model.pkl")
    feature_names = joblib.load("feature_names.pkl")
    return departure_model, arrival_model, feature_names

departure_model, arrival_model, feature_names = load_models()

# ============================================
# HEADER
# ============================================

st.title("✈️ Flight Delay Prediction Dashboard")
st.markdown(
    "Predict **Departure Delay** and **Arrival Delay** using Machine Learning."
)

# ============================================
# SIDEBAR
# ============================================

st.sidebar.header("✈️ Flight Information")

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
    "Weather Condition",
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

# ============================================
# FLIGHT METRICS
# ============================================

st.sidebar.header("📊 Flight Metrics")

distance = st.sidebar.number_input("Distance (KM)", value=1200)

passenger_load = st.sidebar.number_input(
    "Passenger Load Factor (%)",
    value=85.0
)

airline_rating = st.sidebar.number_input(
    "Airline Rating",
    value=0.50
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

# ============================================
# WEATHER
# ============================================

st.sidebar.header("🌦 Weather Details")

wind = st.sidebar.number_input(
    "Wind Speed",
    value=10
)

precip = st.sidebar.number_input(
    "Precipitation",
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

# ============================================
# DATE
# ============================================

st.sidebar.header("📅 Date")

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

# ============================================
# TIME
# ============================================

st.sidebar.header("🕒 Schedule")

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

# ============================================
# INPUT DATAFRAME
# ============================================

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
    "Departure_Minute": departure_minute,
    "Arrival_Hour": arrival_hour,
    "Arrival_Minute": arrival_minute,
}

input_df = pd.DataFrame([input_data])

# ============================================
# ENCODING
# ============================================

input_df["From_BOM"] = 1 if from_airport == "BOM" else 0
input_df["From_CCU"] = 1 if from_airport == "CCU" else 0
input_df["From_DEL"] = 1 if from_airport == "DEL" else 0

input_df["To_DEL"] = 1 if to_airport == "DEL" else 0
input_df["To_HYD"] = 1 if to_airport == "HYD" else 0

airlines = [
    "Air India",
    "Go Air",
    "Indigo",
    "SpiceJet",
    "Spicejet",
    "Vistara"
]

for a in airlines:
    input_df[f"Airline_{a}"] = 1 if airline == a else 0

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
    input_df[f"weather__hourly__weatherDesc__value_{w}"] = (
        1 if weather == w else 0
    )

for i in [1, 2, 3, 4]:
    input_df[f"Category_{i}"] = (
        1 if category == i else 0
    )

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Saturday",
    "Sunday"
]

for d in weekdays:
    input_df[f"Weekday_{d}"] = (
        1 if weekday == d else 0
    )

input_df = input_df.reindex(
    columns=feature_names,
    fill_value=0
)

# ============================================
# PREDICTION
# ============================================

if st.button(
    "✈️ Predict Flight Delay",
    use_container_width=True
):

    departure_delay = round(
        departure_model.predict(input_df)[0],
        2
    )

    arrival_delay = round(
        arrival_model.predict(input_df)[0],
        2
    )

    weather_risk = round(
        (
            humidity * 0.25 +
            wind * 0.30 +
            precip * 0.30 +
            cloudcover * 0.15
        ),
        2
    )

    route_score = round(
        (
            otp_index * 0.5 +
            airline_rating * 20 +
            airport_rating * 20
        ),
        2
    )

    overall_risk = round(
        (departure_delay + arrival_delay) / 2,
        2
    )

    st.success("Prediction Completed Successfully ✅")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "✈️ Departure Delay",
        f"{departure_delay} min"
    )

    col2.metric(
        "🛬 Arrival Delay",
        f"{arrival_delay} min"
    )

    col3.metric(
        "🌦 Weather Risk",
        weather_risk
    )

    col4.metric(
        "📊 Route Score",
        route_score
    )

    st.markdown("---")

    st.subheader("🚦 Delay Risk Assessment")

    if overall_risk <= 15:
        st.success(
            f"🟢 Low Delay Risk ({overall_risk} min)"
        )
    elif overall_risk <= 45:
        st.warning(
            f"🟡 Medium Delay Risk ({overall_risk} min)"
        )
    else:
        st.error(
            f"🔴 High Delay Risk ({overall_risk} min)"
        )

    st.markdown("---")

    st.subheader("📋 Flight Summary")

    st.write(f"**Route:** {from_airport} → {to_airport}")
    st.write(f"**Airline:** {airline}")
    st.write(f"**Weather:** {weather}")
    st.write(f"**Distance:** {distance} KM")

    st.write(
        f"**Departure:** "
        f"{departure_hour:02d}:{departure_minute:02d}"
    )

    st.write(
        f"**Arrival:** "
        f"{arrival_hour:02d}:{arrival_minute:02d}"
    )

    st.markdown("---")

    report = pd.DataFrame({
        "Prediction Time": [datetime.now()],
        "From": [from_airport],
        "To": [to_airport],
        "Airline": [airline],
        "Weather": [weather],
        "Departure Delay": [departure_delay],
        "Arrival Delay": [arrival_delay]
    })

    st.download_button(
        label="📥 Download Prediction Report",
        data=report.to_csv(index=False),
        file_name="flight_prediction_report.csv",
        mime="text/csv"
    )

    with st.expander("🔍 View Model Features"):
        st.dataframe(input_df)

# ============================================
# SIDEBAR INFO
# ============================================

st.sidebar.markdown("---")

st.sidebar.info(
    """
### Project Information

**Model:** XGBoost

**Framework:** Streamlit

**Predictions:**
- Departure Delay
- Arrival Delay

**Developer:**
Chaitanya Nadapuri
"""
)

# ============================================
# FOOTER
# ============================================

st.markdown("---")

st.subheader("📊 About Project")

st.write("""
This system predicts flight delays using
historical airline, airport, route and
weather data.

Features:
- Flight Delay Prediction
- Weather Risk Analysis
- Route Performance Score
- Downloadable Reports
- Machine Learning Powered Decision Support
""")

st.caption(
    "© 2026 Flight Delay Prediction Dashboard"
)
