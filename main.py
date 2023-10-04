# Initial commit:
# First commit:
import requests
import os
# import json
import datetime

CURRENT = datetime.datetime.now()

sheety_url = "https://api.sheety.co/792a621e9a95f9932e7a7e96c1680077/workoutTracking/workouts"
sheety_headers = {
    "Authorization": "Basic d2FueXVkZXZ0ZXN0OmRzaGprZmh3aXVpZHNramdmbGRqZmts"
}

sheety_get_response = requests.get(sheety_url, headers=sheety_headers)
print(sheety_get_response.text)

# sheety_data = sheety_get_response.text
# print(sheety_data["workouts"][0])


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
#---------------------------------------------------------------------------------------------------
data = response.json()
# print(data)
for item in data["exercises"]:
    # print(item)
    # for key, value in item.items():
    #     print(key, value)

    # We actually don't need to make it too commplicated:
    items = {key: value for key, value in item.items()
             if 0 < list(item.keys()).index(key) < 5 and
             list(item.keys()).index(key) != 3}
    # print(items)

    # print(type(items))

    # Same as first_5_items, no need to change again:
    # data = json.dumps(first_5_items)
    # print(data)
    # print(type(data))
    new_items = []
    for key, value in items.items():
    #     # print((key, value).json())
        new_items.append(value)
    # print(new_items)
# Prepare my spreadsheet: READY!
#------------------------------------------------------------------------------------------------
# Start to make requests through Sheety API:

    sheety_params = {
        "workout": {
            "date": CURRENT.strftime("%d/%m/%Y"),
            "time": CURRENT.strftime("%H:%M:%S"),
            "exercise": new_items[0],
            "duration": new_items[1],
            "calories": new_items[2],
        }
    }
    sheety_response = requests.post(sheety_url, json=sheety_params, headers=sheety_headers)
    print(sheety_response.text)
# Perfectly done with all the rest!
#---------------------------------------------------------------------------------------------