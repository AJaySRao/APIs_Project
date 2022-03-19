import requests
from datetime import datetime, timezone
import smtplib
import time

LAT = 16.544893
LNG = 81.521240
EMAIL = "samplgemail9@gmail.com"
PASS = "9samplegmail"


def iss_in_local_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    if LAT-5 <= iss_lat <= LAT+5 and LNG-5 <= iss_lng <= LNG+5:
        return True


def mid_night():
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0
    }

    res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters,)
    res.raise_for_status()
    data = res.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now(timezone.utc).hour
    if current_time >= sunset or current_time <= sunrise:
        return True




