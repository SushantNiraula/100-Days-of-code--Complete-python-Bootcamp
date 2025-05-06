# with open('weather_data.csv') as csvfile:
#     weathers=csvfile.readlines()
#     print(weathers)

import csv
with open('weather_data.csv', newline='') as csvfile:
    data=csv.reader(csvfile)
    temp=[]
    print(data)
    for row in data:
        if row[1]!='temp':
            temp.append(int(row[1]))
    print(temp)