# Initial commit:
# First commit:
import requests
import os
# import json
import datetime

GENDER = "female"
WEIGHT_KG = 57.5
HEIGHT_CM = 169.5
AGE = 34

application_id = os.environ.get("APPLICATION_ID")
api_keys = os.environ.get("API_KEYS")

query = input(f"How's today's workout?\n"
              f"(ex: I ran 3 miles and walked 2 miles)\n(or: "
              f"30 min yoga) \nAnswer: ").lower()
# gender = input(f" What's your gender? (Female/Male): ").lower()
# weight_kg = float(input(f"Kg: "))
# height_cm = float(input(f"Cm: "))
# age = int(input(f"Age: "))


exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_params = {
    "query":query,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

headers = {
    "x-app-id": application_id,
    "x-app-key": api_keys,
    # "Content-Type": "application/json"
}

response = requests.post(exercise_endpoints,
                         json=user_params, headers=headers)
# print(response.text)
# print((response.json()))
# Perfectly done by myself!
# Small adjust to fit with Dr.Angela's codes.
#------------------------------------------------------------------------
data = response.json()
# print(data)
for item in data["exercises"]:
    # print(item)
    # for key, value in item.items():
    #     print(key, value)
    items = {key: value for key, value in item.items()
             if 0 < list(item.keys()).index(key) < 5}
    # print(items)
    # print(type(items))

    # Same as first_5_items, no need to change again:
    # data = json.dumps(first_5_items)
    # print(data)
    # print(type(data))

    # for key, value in first_5_items.items():
    #     print((key, value).json())

# Prepare my spreadsheet: READY!


