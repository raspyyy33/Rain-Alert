# ☔ Rain Alert App

A lightweight Python script that checks the weather forecast for your location and sends you an email reminder to bring an umbrella if rain is expected in the next 12 hours.

## How It Works

The app queries the [OpenWeatherMap Forecast API](https://openweathermap.org/forecast5) for the next 4 time slots (12 hours) at your coordinates. If any slot has a weather condition code below 700 — which covers all rain, snow, and storm conditions — it fires off an email alert to you.

## Prerequisites

- Python 3.x
- A free [OpenWeatherMap](https://openweathermap.org/api) API key
- A Gmail account (with [App Passwords](https://support.google.com/accounts/answer/185833) enabled if you use 2FA)

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/your-username/rain-alert.git
   cd rain-alert
```

2. Install the required dependency:
```bash
   pip install requests
```

## Configuration

The app reads all sensitive values from environment variables — no hardcoded credentials.

| Variable | Description |
|---|---|
| `API_KEY` | Your OpenWeatherMap API key |
| `MY_LAT` | Your latitude (e.g. `23.8103`) |
| `MY_LONG` | Your longitude (e.g. `90.4125`) |
| `MY_EMAIL` | Your Gmail address |
| `MY_PASS` | Your Gmail password or App Password |

Set them in your terminal before running:

```bash
export API_KEY="your_openweathermap_api_key"
export MY_LAT="23.8103"
export MY_LONG="90.4125"
export MY_EMAIL="you@gmail.com"
export MY_PASS="your_app_password"
```

Or on Windows (Command Prompt):

```cmd
set API_KEY=your_openweathermap_api_key
set MY_LAT=23.8103
set MY_LONG=90.4125
set MY_EMAIL=you@gmail.com
set MY_PASS=your_app_password
```

## Usage

```bash
python main.py
```

If rain is detected in the next 12 hours, you'll receive an email with the subject **"Rain Incoming!"** and a friendly reminder to grab your umbrella.

## Gmail Setup

Standard Gmail passwords may be blocked by Google for third-party apps. To fix this:

1. Enable 2-Step Verification on your Google account.
2. Go to **Google Account → Security → App Passwords**.
3. Generate an app password and use it as your `MY_PASS` value.

## Automating the Script

To get daily alerts automatically, you can schedule the script using:

- **Linux/macOS** — `cron`:
```bash
  # Run every morning at 7am
  0 7 * * * /usr/bin/python3 /path/to/main.py
```
- **Windows** — Task Scheduler

## Weather Condition Codes

OpenWeatherMap uses numeric codes to classify weather. Codes below 700 include:

| Range | Category |
|---|---|
| 200–299 | Thunderstorm |
| 300–399 | Drizzle |
| 500–599 | Rain |
| 600–699 | Snow |

Any of these will trigger an alert. Clear skies, clouds, fog, and other conditions (700+) will not.

## License

This project is open source and available under the [MIT License](LICENSE).
