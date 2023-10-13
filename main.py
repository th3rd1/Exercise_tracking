import requests
from datetime import datetime
import os

sheety_token = os.environ["sheety_token"]
nutritionix_api_key = os.environ["nutritionix_api_key"]
nutritionix_app_id = os.environ["nutritionix_app_id"]
sheety_add_endpoint = os.environ["sheety_add_endpoint"]

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


exercise_text = input("Tell me which exercises you did: ")

nutritionix_exercise_params = {
 "query": exercise_text,
 "gender": "male",
 "weight_kg": 83.91,
 "height_cm": 182.88,
 "age": 29
}

headers = {
    "x-app-id": nutritionix_app_id,
    'x-app-key': nutritionix_api_key
}

sheety_headers = {
    "Authorization": f"Bearer {sheety_token}",
    "Content-Type": "application/json"
}

response = requests.post(url=nutritionix_exercise_endpoint, json=nutritionix_exercise_params, headers=headers)
result = response.json()

today = datetime.now()
today_date = today.strftime("%x")
today_time = today.strftime("%X")
exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]



for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_add_endpoint, json=sheet_inputs, headers=sheety_headers)
print(sheet_response.text)
