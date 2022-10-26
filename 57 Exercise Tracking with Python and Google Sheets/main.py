import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 64
HEIGHT_CM = 150
AGE = 19

APP_ID = "dfb4ab36"
API_KEY = "744fd32b85aeeec578a183a1d1d1a142"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e2d8e899d4ab3456485fcd08c0645b10/myWorkouts (day38)/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

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

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

YOUR_USERNAME = "kritika05"
YOUR_PASSWORD = "2003@me*14"

sheet_response = requests.post(
  url=sheet_endpoint,
  json=sheet_inputs,
  auth=(
      YOUR_USERNAME,
      YOUR_PASSWORD,
  )
)