import requests
import json
import os 
API_KEY= os.environ.get('OWM_API_KEY')
lat=27.712021
lon=85.312950
OWM_Endpoint='https://api.openweathermap.org/data/2.5/forecast'
params={
    'lat':lat,
    'lon':lon,
    'appid':API_KEY,
    'units':'metric',
    'cnt':4,
}
response= requests.get(OWM_Endpoint, params=params)
print(response.status_code)
response.raise_for_status()

data= response.json()
print(json.dumps(data, indent=4))
json.dump(data, open('weather_data.json', 'w'), indent=4)
