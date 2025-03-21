from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from ler_credenciais import emailLinkedin
from ler_credenciais import senhaLinkedin

# Setup Selenium with automatic WebDriver management
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Open browser
driver = webdriver.Chrome(service=service, options=options)

# Open Google
driver.get("https://www.linkedin.com/")


botaoEntrarLinkedin = driver.find_element(By.XPATH, "/html/body/nav/div/a[normalize-space(text())='Entrar']")
botaoEntrarLinkedin.click()
print("Button pressed")

campoUserLogin =  driver.find_element(By.ID, "username")
campoSenhaLogin =  driver.find_element(By.ID, "password")
campoUserLogin.send_keys(emailLinkedin)
campoSenhaLogin.send_keys(senhaLinkedin)


#botaoEntrarLinkedin = driver.find_element(By.XPATH, "/html/body/nav/div/a[normalize-space(text())='Entrar']").click()

#botao =  driver.find_element(By.ID, "password")


import time
time.sleep(2)

input("Esperar")