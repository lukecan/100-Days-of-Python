# Workout Tracker

This code allows you to track your workouts by logging exercises and keeping track of progress. It uses the Nutritionix API and the Sheety API. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed on your machine:

- Python3
- Requests library
- dotenv library

### Installing

1. Clone or download the repository
2. Create a .env file in the root of the project and add the following environment variables:
    - NUTRI_ID
    - NUTRI_KEY
    - GENDER
    - WEIGHT_KG
    - HEIGHT_CM
    - AGE
    - SHEETY_USER
    - SHEETY_PASS
3. Run the code using `python3 main.py`

## Functionality

1. The `get_exercise` function prompts the user to input the exercise they did, makes a request to the Nutritionix API to get information about the exercise, and returns a workout dictionary with the date, time, exercise name, duration, and calories burned.

2. The `get_doc` function makes a GET request to the Sheety API to get all the stored workouts.

3. The `log_exercise` function logs the workout by making a POST request to the Sheety API and passing the workout dictionary.

4. The `get_date` function returns the current date in the format "dd/mm/yyyy".

5. The `get_time` function returns the current time in the format "hh:mm:ss".

6. The `log_exercise` function is called with the result of the `get_exercise` function, and the results of the `get_date` and `get_time` functions as arguments.

## Built With

- [Python3](https://www.python.org/) - The programming language used
- [Requests library](https://requests.readthedocs.io/en/master/) - For making HTTP requests
- [dotenv library](https://pypi.org/project/python-dotenv/) - For loading environment variables
