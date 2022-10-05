from data_manager import DataManager
from flight_search import FlightSearch
from datetime import timedelta, datetime
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
ORGN_CITY_IATA = "ICN"


if sheet_data[0]["iataCode"]:
    pass
else:
    for row in sheet_data:
        print(row["city"])
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.sheet_data = sheet_data
    data_manager.put_destination_data()


tomorrow = (datetime.now() + timedelta(1)).strftime("%d/%m/%Y")
six_month_from_today = (datetime.now() + timedelta(6*30)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORGN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ₩{flight.price} to fly from {flight.orgn_city}-{flight.orgn_airport_code} to {flight.destination_city}-{flight.destination_airport_code}, from {flight.out_date} to {flight.return_date}."
        )
