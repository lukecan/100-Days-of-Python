# import necessary modules
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import datetime as dt

# load environment variables from .env file
load_dotenv()


def get_exercise(date, time):
    # set headers for nutritionix API request
    headers = {
        "x-app-id": os.getenv("NUTRI_ID"),
        "x-app-key": os.getenv("NUTRI_KEY"),
    }

    # get exercise text input from user
    exercise_text = input("Tell me which exercises you did: ")

    # set parameters for nutritionix API request
    nutri_params = {
        "query": exercise_text,
        "gender": os.getenv("GENDER"),
        "weight_kg": os.getenv("WEIGHT_KG"),
        "height_cm": os.getenv("HEIGHT_CM"),
        "age": os.getenv("AGE")
    }
    nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    # make request to nutritionix API
    response = requests.post(url=nutri_endpoint, json=nutri_params, headers=headers)

    # parse response
    result = response.json()

    # print the exercise name
    print(result['exercises'][0]['name'])

    # create workout dictionary
    workout = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": result['exercises'][0]['name'].title(),
            "duration": result['exercises'][0]['duration_min'],
            "calories": result['exercises'][0]['nf_calories']
        }
    }
    return workout


def get_doc():
    # make request to sheety API to get all workouts
    sheety_endpoint = "https://api.sheety.co/a1b33429104837e61552199a5b077434/workoutTracking/workouts"
    response = requests.get(url=sheety_endpoint)

    # raise an error if request fails
    response.raise_for_status()

    # parse response
    data = response.json()
    print(data)


def log_exercise(workout):
    # set basic auth for sheety API request
    basic = HTTPBasicAuth(os.getenv("SHEETY_USER"), os.getenv("SHEETY_PASS"))

    # set endpoint for logging workout
    sheety_logging_endpoint = "https://api.sheety.co/a1b33429104837e61552199a5b077434/workoutTracking/workouts"

    # make request to log workout
    response = requests.post(url=sheety_logging_endpoint, json=workout, auth=basic)

    # raise an error if request fails
    response.raise_for_status()

    # print response text
    print(response.text)


def get_date():
    # get current date
    today = dt.datetime.today()

    # format date as "dd/mm/yyyy"
    formatted_today = today.strftime("%d/%m/%Y")
    return formatted_today


def get_time():
    # get current time
    time = dt.datetime.now().time()

    # format time as "hh:mm:ss"
    formatted_time = time.strftime("%H:%M:%S")
    return formatted_time

    # log exercise by calling helper functions


log_exercise(get_exercise(get_date(), get_time()))
