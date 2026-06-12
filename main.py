import requests as requests
import smtplib
import os

api_key = os.environ.get("API_KEY")
mylat = os.environ.get("MY_LAT")
mylong = os.environ.get("MY_LONG")
email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASS")
parameters ={
    "lat": mylat,
    "lon": mylong,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hrdata in data["list"]:
    condition_code = int(hrdata["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg="Subject:Rain Incoming!\nDon't forget to bring an umbrella:)"
    )
