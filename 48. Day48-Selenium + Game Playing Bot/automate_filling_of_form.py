from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')
## We will be filling the form with the following details
first_name = 'John'
last_name = 'Doe'
email='jhondoe10@gmail.com'
## Find the input fields and fill them
time.sleep(2)
first_name_input=driver.find_element(By.NAME, 'fName')
first_name_input.clear()
first_name_input.send_keys(first_name)

time.sleep(2)
last_name_input=driver.find_element(By.NAME, 'lName')
last_name_input.clear()
last_name_input.send_keys(last_name)

time.sleep(2)
email_input=driver.find_element(By.NAME, 'email')
email_input.clear()
email_input.send_keys(email)
time.sleep(2)

submit_button=driver.find_element(By.CSS_SELECTOR,'.form-signin .btn')
submit_button.click()
time.sleep(5)

## close the browser
driver.quit()