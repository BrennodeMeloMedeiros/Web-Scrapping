# Rode esse script se esse for seu primeiro acesso ao linkedin utilizando essa automação.
# Leia README.md
import time
from  selenium.webdriver.common.by import By
from config_driver import configurar_driver

driver = configurar_driver()

driver.get("https://www.linkedin.com/")


botaoEntrarLinkedin = driver.find_element(By.XPATH, "/html/body/nav/div/a[normalize-space(text())='Entrar']")
botaoEntrarLinkedin.click()
print("Preencha suas credenciais do Linkedin")

time.sleep(30)