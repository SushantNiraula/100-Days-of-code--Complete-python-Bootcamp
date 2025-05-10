import requests
import json
from dotenv import load_dotenv
from twilio.rest import Client
import os
load_dotenv()
api_key = os.getenv('OWM_API_KEY')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
client = Client(account_sid, auth_token)

params={
    'lat':27.712021,
    'lon':85.312950,
    'appid':api_key,
    'units':'metric',
    'cnt':4,
}
response= requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
data=response.json()
weather_ids=[]
for i in range(len(data['list'])):
    condition_code=data['list'][i]['weather'][0]['id']
    weather_ids.append(condition_code)
    if int(condition_code)<700:
        will_rain= True
if will_rain:
    message = client.messages.create(
    body="It will rain today. Don't forget to take your umbrella.",
    from_='+kjkd',
    to='+kkjfeoj')
    print(message.status)
