import requests
import json
import os 
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key=os.environ.get('OWM_API_KEY')

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
    print("It will rain")
