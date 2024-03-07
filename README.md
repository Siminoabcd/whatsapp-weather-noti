# Weather Notification Script

This Python script fetches weather data from an external API and sends a notification message via Twilio to a specified phone number. It extracts current weather information and forecasts and composes a message with the details.

## Requirements

- Python 3.12.2
- `requests` library (install via `pip install requests`)
- `twilio` library (install via `pip install twilio`)
- A Twilio account with a verified phone number
- Environment variables stored in a `.env` file containing Twilio and weather API credentials:

TWILIO_ACCOUNT_SID=<Your Twilio account SID>
TWILIO_AUTH_TOKEN=<Your Twilio auth token>
TWILIO_PHONE_NUMBER=<Your Twilio phone number>
YOUR_PHONE_NUMBER=<Your phone number>
WEATHER_API_URL=<Weather API URL>


## Setup

1. Clone this repository to your local machine.

2. Install Python dependencies by running:

pip install -r requirements.txt

3. Create a `.env` file in the root directory of the project and add your Twilio and weather API credentials.

4. Run the script using the following command:



## How It Works

1. The script fetches weather data from the specified weather API URL using the `requests` library.

2. It extracts relevant weather information such as current conditions, temperature, and forecast data.

3. The extracted data is used to compose a notification message.

4. The message is sent to the specified phone number using Twilio's SMS service.

## Customization

- You can customize the message composition and formatting in the `create_message` function to suit your preferences.

- Adjust the schedule or trigger for running the script by integrating it with task schedulers or cron jobs, or by using GitHub Actions for automation.




