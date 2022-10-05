import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from requests.auth import HTTPBasicAuth

load_dotenv()

APP_ID = os.environ.get("NTX_APP_ID")
APP_KEY = os.environ.get("NTX_APP_KEY")


nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json",
}

nutritionix_post_request_body = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 115.5,
    "height_cm": 175.64,
    "age": 28
}

nutritionix_res = requests.post(url=nutritionix_url, json=nutritionix_post_request_body, headers=nutritionix_headers)
nutritionix_res.raise_for_status()
exercises = nutritionix_res.json()['exercises']
print(exercises)

now_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_url = os.environ.get("SHEETY_URL")
USERNAME = os.environ.get("SHEETY_AUTH_USERNAME")
PASSWORD = os.environ.get("SHEETY_AUTH_PASSWORD")
basic = HTTPBasicAuth(USERNAME, PASSWORD)

for exercise in exercises:
    sheety_body = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
            }
        }

    print(sheety_body)
    sheety_res = requests.post(sheety_url, json=sheety_body, auth=basic)
    print(sheety_res.text)
