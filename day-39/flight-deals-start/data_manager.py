import os
from dotenv import load_dotenv
import requests

load_dotenv()


url = os.environ["SHEETY_PRICES_ENDPOINT"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheet_data = {}

    def get_destination_data(self):
        res = requests.get(url=url)
        res.raise_for_status()
        self.sheet_data = res.json()['prices']
        return self.sheet_data

    def put_destination_data(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            res = requests.put(url=f"{url}/{city['id']}", json=new_data)
            res.raise_for_status()
