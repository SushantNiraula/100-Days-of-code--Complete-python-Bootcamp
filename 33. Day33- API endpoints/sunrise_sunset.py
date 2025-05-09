import requests
from datetime import datetime
import smtplib
MY_LAT= 27.712021
MY_LNG= 85.312950
timenow= datetime.now()
my_email="gopalsharma98011@gmail.com"

response=requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
response_json=response.json()
latitude= float(response_json['iss_position']['latitude'])
longitude= float(response_json['iss_position']['longitude'])
iss_colse=False
if MY_LAT-5<=latitude<=MY_LAT+5 and MY_LNG-5<=longitude<=MY_LNG+5:
    iss_colse=True
else:
    iss_colse=False
parameters={
    'lat':MY_LAT,
    'lng':MY_LNG,
    'formatted':0

}
response= requests.get('https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
response_json=response.json()
sunrise=int(response_json['results']['sunrise'].split('T')[1].split(':')[0])
sunset=int(response_json['results']['sunset'].split('T')[1].split(':')[0])
is_dark=False
if timenow.hour>=sunset or timenow.hour<=sunrise:
    is_dark=True
else:
    is_dark=False

if iss_colse and is_dark:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sushantniraula01@gmail.com",
            msg="Subject:Look Up! \n\n The ISS is above you in the sky."
        )
else:
    print("The ISS is not close to you or it's not dark.")
