from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Chrome browser open
driver = webdriver.Chrome()
driver.maximize_window()

# Google open
driver.get("https://www.google.com")

time.sleep(3)

# Search box
search_box = driver.find_element(By.NAME, "q")

text = "zentrovatools.com"

# Human-like typing
for char in text:
    search_box.send_keys(char)
    time.sleep(random.uniform(0.08, 0.25))  # Random delay between keystrokes

# Thoda ruk kar Enter
time.sleep(random.uniform(0.5, 1.2))
search_box.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()
