from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from selenium.webdriver.common.by import By
import time


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

url = 'https://www.nummerplade.net/nummerplade/db91788.html'

driver = webdriver.Chrome(url, chrome_options=opt)
wait = WebDriverWait(driver, 5)

element = driver.find_element("xpath", '//*[@id="box-overblik-data-overblik_forsikring"]/div/small')

print(element)

