import requests
LAT = 16.466510
LNG = 81.478336

parameters = {
    "lat": LAT,
    "lng": LNG
}

res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
res.raise_for_status()
data = res.json()
print(data)
