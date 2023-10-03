# Initial commit:
# First commit:
import requests
import os

application_id = os.environ.get("APPLICATION_ID")
api_keys = os.environ.get("API_KEYS")

query = input(f"How's today's workout? "
              f"(Ex: i ran 3 miles and walked 2 miles ): ").lower()
gender = input(f" What's your gender? (Female/Male): ").lower()
weight_kg = float(input(f"Kg: "))
height_cm = float(input(f"Cm: "))
age = int(input(f"Age: "))

exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_params = {
    "query":query,
    "gender":gender,
    "weight_kg":weight_kg,
    "height_cm":height_cm,
    "age":age
}

headers = {
    "x-app-id": application_id,
    "x-app-key": api_keys,
    "Content-Type": "application/json"
}

response = requests.post(exercise_endpoints,
                         json=user_params, headers=headers)
print(response.json())
# Perfectly done by myself!