from bs4 import BeautifulSoup
import requests
import time
import smtplib 

url='https://www.amazon.in/Ant-Esports-Elite-1100-Mid-Tower/dp/B0CRNQJBWB/ref=sr_1_13?crid=1JGAQVTRDPCCY&dib=eyJ2IjoiMSJ9.qoNFgzy3ZGRvfjidp4IMuneF2iDhbiTT_BVEMOdkcWdV_tly92he4cJdCSVQyLj3vSaa_EiHKVt3NqOHy48QfcRb2RZoq0IDjZZYAVMz-SPDCuOIlkQZBGRWnYwrjaL5JHIRSG0iglEqVay0ePvDuAkFm5qcrEa8chPpHm6QtrQaHBBjgA-T-QAIeVw8EW4twviPYhpKW0tN17O466XInLXcxpGZeXeV38sqtz-XxLo.7RnPzXzuxSDKkF-H5A582_JjJQjqfRyAwCYJ-j9byks&dib_tag=se&keywords=gaming%2Bpc&qid=1747120428&sprefix=gaming%2Bp%2Caps%2C247&sr=8-13&th=1'
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 safari/537.3',

}

response=requests.get(url,headers=header)
webpage=response.content
soup=BeautifulSoup(webpage,'html.parser')
while True:
    try:
        price=soup.find(name='span',class_='a-offscreen').getText()
        break
    except AttributeError:
        print("Price not found, retrying...")
        time.sleep(5)
price=soup.find(name='span',class_='a-offscreen').getText()
our_price=2100
price=price[1:]
price,_=price.split('.')
price=int(price.replace(',',''))
if price<our_price:
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login('gopalsharma98011@gmail.com',)
        connection.sendmail(
            from_addr='gopalsharma98011@gmail.com',
            to_addrs='sushantniraula01@gmail.com',
            msg=f"Subject:Price Drop Alert!\n\nThe price of the product has dropped to {price}.\nCheck it out here: {url}"
        )


