import json
import requests
import datetime
import os

app_id = "185d86bd"
api_key = os.environ['api_key']

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': app_id,
    'x-app-key': api_key}

query = input("Enter the exercise information: ")

params = {"query": query}
response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
data = json.loads(response.text)
print(data)
exercises = data['exercises']

for exe in exercises:
    exercise = exe['name']
    duration = exe['duration_min']
    burnt_calories = exe['nf_calories']
    date = datetime.datetime.now()

    print(f"{exercise},{duration}, {burnt_calories}")
    formatted_date = date.strftime("%d/%m/%Y")
    formatted_time = date.strftime("%H:%M:%S")

    sheety_endpoint = 'https://api.sheety.co/cdba9791ba9fc7e84882b41c9b6ec648/myWorkouts/workouts'
    headers = {"Content-Type": "application/json",
               "Authorization": "Bearer extralongsecrettoken"}

    workout = {"workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise,
        "duration": duration,
        "calories": burnt_calories
    }}

    response = requests.post(url=sheety_endpoint, json=workout, headers=headers)
    print(response.text)