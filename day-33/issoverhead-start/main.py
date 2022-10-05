import requests
from datetime import datetime
import smtplib

MY_LAT = 35.548679 # Your latitude
MY_LONG = 129.315002 # Your longitude

my_email = "test.junpak@gmail.com"
password = "punvhnamdosrfzun"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    # Your position is within +5 or -5 degrees of the ISS position.
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <  iss_longitude < MY_LONG + 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = (int(response.json()["results"]["sunrise"].split('T')[1].split(':')[0]) + 9) % 24
    sunset = (int(response.json()["results"]["sunset"].split('T')[1].split(':')[0]) + 9) % 24

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Look up!! \n\n The ISS is above you in the sky"
            )
