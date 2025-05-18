import requests
from dotenv import load_dotenv
load_dotenv()
import os
weight_kg=75
height_cm=175
age=25
gender='male'
nutritionix_app_id = os.getenv('NUTRITIONIX_APP_ID')
nutritionix_api_key = os.getenv('NUTRITIONIX_API')
headers={
    'Content-Type': 'application/json',
    'x-app-id': '16bde287',
    'x-app-key': '34bc165f23c713eb8eace0d54b8eba13',
}
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
method='POST'
exercise = input("Tell me which exercises you did: ")
params ={
    'query':exercise,
    'gender':gender,
    'weight_kg':weight_kg,
    'height_cm':height_cm,
    'age':age,

}
response=requests.post(url=exercise_endpoint, headers=headers,json=params)
response.raise_for_status()
exercise_data=response.json()
print(exercise_data)