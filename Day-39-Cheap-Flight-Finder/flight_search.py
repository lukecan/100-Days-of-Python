import requests
from dotenv import load_dotenv
import os

from flight_data import FlightData

class FlightSearch:
    def __init__(self):
        # load environment variable
        load_dotenv()
        # get the api key
        self.api_key = os.getenv("KIWI_API_KEY")
        # set the headers
        self.headers = {
            "apikey": self.api_key
        }

    def find_iata(self, city_name):
        # define the endpoint
        endpoint = "https://api.tequila.kiwi.com/locations/query"

        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        data = response.json()["locations"]
        try:
            code = data[0]["code"]
            return code
        except IndexError:
            print(f'No IATA code found for {city_name}')

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": self.api_key
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(
            url="https://api.tequila.kiwi.com/v2/search",
            headers=headers,
            params=query,
        )

        try:
            print(response.json())
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
