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

def create_message(weather_info):
    message = f"Current weather in {weather_info['location_name']}: {weather_info['current_conditions_text']}. Temperature: {weather_info['current_temperature_c']}°C. Feels like: {weather_info['current_feels_like_c']}°C."
    message += f"\nForecast for {weather_info['forecast_date']}: Max temperature: {weather_info['forecast_max_temp_c']}°C, Min temperature: {weather_info['forecast_min_temp_c']}°C, Chance of rain: {weather_info['forecast_chance_of_rain']}%, Forecast conditions: {weather_info['forecast_conditions_text']}."
    message += f"\nSunrise: {weather_info['astro_sunrise']}, Sunset: {weather_info['astro_sunset']}."
    return message

def main():

    # Twilio credentials
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
    my_phone_number = os.getenv('YOUR_PHONE_NUMBER')
    weather_api_url = os.getenv('WEATHER_API_URL')

    # Fetch weather data
    weather_data = fetch_weather_data(weather_api_url)

    # Extract weather information
    weather_info = extract_weather_info(weather_data)

    # Create message
    message = create_message(weather_info)

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=twilio_phone_number,
    body= message,
    to=my_phone_number
    )

if __name__ == "__main__":
    main()