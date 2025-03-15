from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Selenium with automatic WebDriver management
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Open browser
driver = webdriver.Chrome(service=service, options=options)

# Open Google
driver.get("https://www.linkedin.com/")



# A
element = driver.find_element(By.XPATH, "/html/body/nav/div/a[normalize-space(text())='Entrar']")
element.click()
print("Button pressed")

import time
time.sleep(2)