from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = './chromedriver.exe'
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://www.nummerplade.net/')

search = driver.find_element(By.NAME, 'regnr')
search.send_keys('DB91788')
time.sleep(1)
search.send_keys(Keys.RETURN)

time.sleep(5)
insurance = driver.find_element(By.XPATH, '/html/body/div[6]/div[4]/div[2]/ul/li[5]/div/small').text

if insurance == 'Selskab: SELVFORSIKRING':
  print('ALARM: CIVIL POLITI')
else:
  print('Almindelig borger')

driver.quit()

