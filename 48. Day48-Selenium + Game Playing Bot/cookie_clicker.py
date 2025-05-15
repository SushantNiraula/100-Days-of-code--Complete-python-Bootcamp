from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
cookies=driver.get('https://orteil.dashnet.org/experiments/cookie/')
actual_cookie= driver.find_element(By.ID, 'cookie')
## count for 5 seconds

while True:
    timeout = time.time() + 60*5
    if time.time() > timeout:
        
    actual_cookie.click()

driver.quit()
