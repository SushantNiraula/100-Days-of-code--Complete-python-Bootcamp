STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import json

import os 
from dotenv import load_dotenv
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))
load_dotenv()
aplha_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_url='https://www.alphavantage.co/query?'

params={
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':aplha_api_key,
    'outputsize':'compact'
}
response=requests.get(alpha_url, params=params)
response.raise_for_status()
data=response.json()
time_data=data['Time Series (Daily)']
dates=list(time_data.keys())
yesterday=dates[0]
day_before=dates[1]
if time_data[yesterday]['4. close']> time_data[day_before]['4. close'] or time_data[yesterday]['4. close']< time_data[day_before]['4. close']:
    percent_change=(float(time_data[yesterday]['4. close'])-float(time_data[day_before]['4. close']))/float(time_data[day_before]['4. close'])*100
    articles=newsapi.get_everything(q=COMPANY_NAME,
                from_param=yesterday,
                to=yesterday,
                language='en',
                sort_by='relevancy',
                page_size=3)
    msg=[]
    for article in articles['articles']:
        title=article['title']
        description=article['description']
        url=article['url']
        msg={
        'title':title,
        'description':description,
        }
   
    if percent_change>4:
        print("Get News")
        print(f"{COMPANY_NAME}: 🔺{round(percent_change, 2)}%")
    elif percent_change<-4:
        print("Get News")
        print(f"{COMPANY_NAME}: 🔻{round(percent_change, 2)}%")
    else:
        print("No news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

