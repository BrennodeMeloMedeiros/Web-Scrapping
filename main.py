import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


campoUserLogin =  driver.find_element(By.ID, "username")
campoSenhaLogin =  driver.find_element(By.ID, "password")
campoUserLogin.send_keys(emailLinkedin)
campoSenhaLogin.send_keys(senhaLinkedin)


#botaoEntrarLinkedin = driver.find_element(By.XPATH, "/html/body/nav/div/a[normalize-space(text())='Entrar']").click()

#botao =  driver.find_element(By.ID, "password")

time.sleep(2)

input("Esperar")