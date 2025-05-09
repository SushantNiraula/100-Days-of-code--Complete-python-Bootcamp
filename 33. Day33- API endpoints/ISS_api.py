import requests as re

response=re.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
response_json=response.json()
latitude=response_json['iss_position']['latitude']
longitude=response_json['iss_position']['longitude']