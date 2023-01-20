from dotenv import load_dotenv
import requests

class DataManager:
    # Initialize variables
    def __init__(self):
        self.destination_data = {}
        load_dotenv()
        self.endpoint = "https://api.sheety.co/a1b33429104837e61552199a5b077434/flightDeals/prices"

    # Get data from API
    def get_doc(self):
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        print(response.text)
        return self.destination_data

    # Add IATA codes to each city
    def add_iata_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{self.endpoint}/{city['id']}", json=new_data)
            print(response.text)
