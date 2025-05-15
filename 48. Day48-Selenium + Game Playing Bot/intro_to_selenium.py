from selenium import webdriver
from selenium.webdriver.common.by import By
#3 keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver =webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.in/Acer-Processor-LED-Backlit-Win11Home-A324-51/dp/B0D9QLPY8B/ref=sr_1_1_sspa?crid=3E29S5Y82WNE4&dib=eyJ2IjoiMSJ9.TLd7AHpXCFyM48gLOk64ilI9SBCnC1Q5YxFkWUO9XUooDcbx1Ry_XJhxGzemdZjMh6BBFPLT-bsMDzP2HIaQb-Ho1U1c8NK4Wx1MC7RQlPZQMFHbiTY-aOTXfEtlZKOiBOIYSdrjt4-yxKVllnUL0Lzr48psnHyBNyPJlSHnFlTXrd1mysG-7XY8kSGgmresNCUvmW_f5aW2pIvVVqXN-F6iy8_MhYGhCVcEAURAdlo.c_2hdZirqC69aQI3irrXGBzkaFgRGcgpQ5HSosE4Zp4&dib_tag=se&keywords=acer%2Baspire%2B3&nsdOptOutParam=true&qid=1747140574&sprefix=%2Caps%2C203&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1')
price=driver.find_element(By.CLASS_NAME, value='a-price-whole').text
print(f'The price of the product is {price}')


