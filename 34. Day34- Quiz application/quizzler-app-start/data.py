import json
import requests

response= requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
response.raise_for_status()
in_json= response.json()

question_data= in_json['results']
