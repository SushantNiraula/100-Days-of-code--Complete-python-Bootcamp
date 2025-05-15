from selenium import webdriver
from selenium.webdriver.common.by import By
#3 keep chrome open
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
page=driver.get('https://en.wikipedia.org/wiki/Main_Page')
#4 find the element
editors=driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
#5 get the text
editors_text=editors.text
print(editors_text)
