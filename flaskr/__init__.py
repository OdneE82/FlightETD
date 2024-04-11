import os
from flask import Flask, jsonify, redirect
import requests
import numpy as np
import xml.etree.ElementTree as ET
import pytz
from datetime import datetime, timedelta
import pickle
import joblib

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
ENCODER_PATH = os.path.join(BASE_DIR, 'airport_encoder.joblib')

with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

encoder = joblib.load(ENCODER_PATH)

def make_prediction(features):
    return model.predict([features])[0]

def convert_time(schedule_time_str, to_timezone='Europe/Oslo'):
    utc_time = datetime.strptime(schedule_time_str, "%Y-%m-%dT%H:%M:%SZ")
    utc_time = utc_time.replace(tzinfo=pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone(to_timezone))
    readable_time = local_time.strftime("%B %d, %Y, %H:%M")
    return readable_time

def calculate_std_minutes(std_time_str):
    std_time = datetime.strptime(std_time_str, "%Y-%m-%dT%H:%M:%SZ")
    std_minutes = std_time.hour * 60 + std_time.minute
    return std_minutes

from datetime import datetime, timedelta
import pytz

def format_etd_prediction(flight_date_str, etd_prediction_minutes, to_timezone='Europe/Oslo'):
    # Parse the flight date
    flight_date = datetime.strptime(flight_date_str, "%Y-%m-%d")
    
    # Calculate the ETD datetime by adding the predicted minutes to the flight date
    # This creates a datetime object for the ETD in UTC
    etd_datetime_utc = flight_date + timedelta(minutes=etd_prediction_minutes)
    
    # Convert the ETD datetime to a string in ISO 8601 format
    etd_datetime_str_utc = etd_datetime_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Use the convert_time function to convert the ETD from UTC to 'Europe/Oslo' time
    formatted_etd = convert_time(etd_datetime_str_utc, to_timezone)
    
    return formatted_etd




def fetch_and_parse_xml(airport_code='BGO', direction='D'):
    url = f'https://flydata.avinor.no/XmlFeed.asp?airport={airport_code}&direction={direction}'
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        flights = []
        for flight in root.findall('.//flight'):
            if flight.find('airline').text == "WF":
                
                flight_out = int(flight.find('flight_id').text[2:])
                destination = flight.find('airport').text
                encoded_destination = encoder.transform([destination])[0]
                day_of_week = datetime.now().weekday()
                month = datetime.now().month
                std = flight.find('schedule_time').text
                std_minutes = calculate_std_minutes(std)

                features = [flight_out, encoded_destination, day_of_week, month, std_minutes]
                flight_date_str = flight.find('schedule_time').text[:10]  # Extract the date part
                etd_prediction = make_prediction(features)
                formatted_etd = format_etd_prediction(flight_date_str, etd_prediction)

                flight_data = {
                    'flightId': flight.find('flight_id').text,
                    'schedule_time': convert_time(std),
                    'airport': flight.find('airport').text,
                    'etd_prediction': formatted_etd,
                }
                flights.append(flight_data)
        return flights
    else:
        return []
    
@app.route('/')
def index():
    # Redirect to the desired default route
    return redirect('/flights/BGO/D')

@app.route('/flights/<airport_code>/<direction>')
def flights(airport_code, direction):
    flights = fetch_and_parse_xml(airport_code, direction)
    return jsonify(flights)

if __name__ == '__main__':
    app.run(debug=True,)