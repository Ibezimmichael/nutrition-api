import requests
from datetime import datetime
import os

NUTRI_API_KEY = os.environ.get("NUTRI_API_KEY")
NUTRI_API_ID = os.environ.get("NUTRI_API_ID")
Nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/17bb8d4367ea7216b8e058cc9d0fe1ef/myWorkouts/workouts"
exercise = input("what did you do for workout today? ")
header = {
    "x-app-id": NUTRI_API_ID,
    "x-app-key": NUTRI_API_KEY,
}
exercise_graph = {
    "query": exercise,
    "height_cm": 190,
    "weight_kg": 118,
    "age": 28,
    "gender": "male"
}
today_date = datetime.now().strftime("%d/%m/%Y")
print(today_date)
now_time = datetime.now().strftime("%X")
print(now_time)
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
response = requests.post(url=Nutri_endpoint, json=exercise_graph, headers=header)
result = response.json()
print(result)


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    bearer_headers = {
        'Content-Type': 'application/json',
        "Authorization": BEARER_TOKEN
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
