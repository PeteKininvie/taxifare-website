import streamlit as st
import requests
from datetime import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
# Date and Time
ride_date = st.date_input("Select ride date", value=datetime.now().date())
ride_time = st.time_input("Select ride time", value=datetime.now().time())

# Combine date and time into a single datetime object
ride_datetime = datetime.combine(ride_date, ride_time)

# Pickup longitude and latitude
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)

# Dropoff longitude and latitude
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

# Passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''


2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
if st.button("Predict Fare"):
    # Build the dictionary containing API parameters
    params = {
        "pickup_datetime": ride_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Call the API using requests
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        prediction = response.json().get("fare", "Prediction not available")

        # Display the prediction
        st.success(f"Estimated Fare: ${prediction:.2f}")

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
