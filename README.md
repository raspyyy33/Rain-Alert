A simple Python application that checks the weather forecast using the OpenWeather API and sends an email notification if rain is expected within the next few hours.

Features
Retrieves weather forecast data from OpenWeather
Detects rain based on weather condition codes
Sends an email alert when rain is forecasted
Uses environment variables to securely store sensitive information
Technologies Used
Python
OpenWeather API
Requests
SMTP (Gmail)
Environment Variables
How It Works
Fetches weather forecast data for a specified location.
Checks the upcoming forecast periods for rain-related weather conditions.
If rain is detected, an email reminder is automatically sent.
The notification reminds the user to bring an umbrella.
Environment Variables

Create the following environment variables:

API_KEY=your_openweather_api_key
MY_LAT=your_latitude
MY_LONG=your_longitude
MY_EMAIL=your_email_address
MY_PASS=your_email_password
Installation
pip install requests
Usage
python main.py
Example Notification
Subject: Rain Incoming!

Don't forget to bring an umbrella :)
Future Improvements
SMS notifications
Support for multiple locations
Daily weather summaries
Desktop and mobile notifications
Weather dashboard with GUI
License

This project is open-source and available under the MIT License.
