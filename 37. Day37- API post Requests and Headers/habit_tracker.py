import requests
import datetime
date=datetime.datetime.now()
date=date.strftime('%Y%m%d')
TOKEN='eihrih328h34jjknfdjhfuh83'
USERNAME='sushantniraula'
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'
user_params={ 
    'token':TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
graph_config={
    'id':'graph2025',
    'name':'Coding Graph',
    'unit':'hr',
    'type':'float',
    'color':'sora',
}
headers={
    "X-USER-TOKEN":TOKEN
}
print('date:',date)
# response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_post_endpooint=f'{graph_endpoint}/graph2025'
graph_data={
    'date':date,
    'quantity':'10',
}
response=requests.post(url=graph_post_endpooint, json=graph_data, headers=headers)
print(response.text)