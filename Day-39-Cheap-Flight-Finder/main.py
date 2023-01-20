from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

# Create instances of DataManager, FlightSearch, and NotificationManager
data_manager = DataManager()
sheet_data = data_manager.get_doc()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set the origin city IATA code
ORIGIN_CITY_IATA = "IST"

# If there is no IATA code for the destinations in sheet_data
if sheet_data[0]["iataCode"] == "":
    # Loop through sheet_data and get the IATA code for each destination
    for row in sheet_data:
        row["iataCode"] = flight_search.find_iata(row["city"])

    # Update the destination_data variable in the DataManager instance with the new IATA codes
    data_manager.destination_data = sheet_data
    data_manager.add_iata_codes()

# Get tomorrow's date and 6 months from today's date
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Loop through destinations and check for flight deals
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # Check if a cheaper flight was found and send a notification if so
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
