import os
from dotenv import load_dotenv
import requests
from flight_data import FlightData

load_dotenv()


TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city):
        url = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        parameters = {
            "term": city,
            "location_types": "city"
        }
        res = requests.get(url=url, params=parameters, headers=headers)
        res.raise_for_status()
        result = res.json()["locations"][0]["code"]
        return result

    def check_flights(self, orgn_airport_code, destination_airport_code, from_time, to_time):
        url = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        parameters = {
            "fly_from": orgn_airport_code,
            "fly_to": destination_airport_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "KRW"
        }
        res = requests.get(url=url, params=parameters, headers=headers)
        res.raise_for_status()
        try:
            data = res.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_airport_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            orgn_city=data["route"][0]["cityFrom"],
            orgn_airport_code=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport_code=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ₩{flight_data.price}")
        return flight_data
