from selenium import webdriver
from selenium.webdriver.common.by import By
#3 keep chrome open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver =webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')
#4 find the element
event=driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul')
#5 get the text
event_text=event.text
event_list=event_text.split('\n')
print(event_list)
dict_events={i//2:{event_list[i]: event_list[i+1]} for i in range(0,len(event_list),2) }
print(dict_events)
# print(event_text)