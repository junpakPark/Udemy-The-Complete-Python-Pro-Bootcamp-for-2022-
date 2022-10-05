import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# print(response.json())

parm = {
    "lat": 35.548679,
    "lng": 129.315002,
    "formatted": 0,
}

# response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={parm['lat']}&lng={parm['lng']}")
response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parm)
response.raise_for_status()
sunrise = (int(response.json()["results"]["sunrise"].split('T')[1].split(':')[0]) + 9) % 24
sunset = (int(response.json()["results"]["sunset"].split('T')[1].split(':')[0]) + 9) % 24

print(sunrise, sunset)

time_now = datetime.now()
print(time_now)
