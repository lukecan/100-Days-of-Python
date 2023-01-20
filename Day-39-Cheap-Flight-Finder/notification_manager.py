from twilio.rest import Client
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# get Twilio SID, Auth token, and phone numbers
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("MY_NUMBER")

class NotificationManager:

    def __init__(self):
        # create a Twilio client using SID and Auth token
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        # create a message using the Twilio client
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
