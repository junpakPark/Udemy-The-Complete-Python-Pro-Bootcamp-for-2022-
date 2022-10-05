class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, orgn_city, orgn_airport_code, destination_city, destination_airport_code, out_date, return_date) -> None:
        self.price = price
        self.orgn_city = orgn_city
        self.orgn_airport_code = orgn_airport_code
        self.destination_city = destination_city
        self.destination_airport_code = destination_airport_code
        self.out_date = out_date
        self.return_date = return_date
