import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to fetch weather data from the API
def fetch_weather_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Function to extract weather information
def extract_weather_info(data):
    location = data['location']
    current = data['current']
    forecast_day = data['forecast']['forecastday'][0]['day']
    astro = data['forecast']['forecastday'][0]['astro']

    # Check if the 'date' key exists in forecast_day
    forecast_date = forecast_day.get('date', 'N/A')

    return {
        'location_name': location['name'],
        'current_temperature_c': current['temp_c'],
        'current_conditions_text': current['condition']['text'],
        'current_feels_like_c': current['feelslike_c'],
        'forecast_date': forecast_date,
        'forecast_max_temp_c': forecast_day.get('maxtemp_c', 'N/A'),
        'forecast_min_temp_c': forecast_day.get('mintemp_c', 'N/A'),
        'forecast_chance_of_rain': forecast_day.get('daily_chance_of_rain', 'N/A'),
        'forecast_conditions_text': forecast_day['condition']['text'] if 'condition' in forecast_day else 'N/A',
        'astro_sunrise': astro.get('sunrise', 'N/A'),
        'astro_sunset': astro.get('sunset', 'N/A')
    }