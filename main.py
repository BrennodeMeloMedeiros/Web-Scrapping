import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from ler_credenciais import emailLinkedin, senhaLinkedin, userAgentNavegador


service = Service(ChromeDriverManager().install())

# Considerando que devemos tomar cuidado para que a conta não seja bloqueada por ser um bot, sera necessário simular comportamentos de um humano no crawler
# Essa simulação começa com as configuração do Chrome que será utilizado pelo Selenium:
options = webdriver.ChromeOptions()

# - Disable Blink:
# Parece que o Chromium utiliza uma engine chamada "Blink" para rodar automações no navegador.
# Essa engine anuncia para o JavaScript que está sendo utilizado ao abrir um site, então precisamos desativar isso para que não seja dectável. 
options.add_argument("--disable-blink-features=AutomationControlled")

# Maximaze Window
# - Isso é um pouco Overkill, mas pode ajudar. O código abaixo garante que o navegador vai ser aberto em tela cheia, já que o tamanho da tela é um dos indicadores de que não é humano acessando o site. 
options.add_argument("--start-maximized")

# - USER-AGENT:
# É um argumento enviado para o site com algumas informações sobre o seu navegador. O selenium usar um user-agent genérico, então aplicar esse diferencial é uma boa vantagem
options.add_argument(
    f'--user-agent={userAgentNavegador}'
)

# - Desativar enable-automation
# A opção de "enable-automation" é umas das formas que o Selenium informa o site que é uma automaçã oque está acessando ele. 
# Ele é responsével pelo banner de “Chrome is being controlled by automated test software” e por modificar alguns objetos que o JavaScript pode ler para saber se é uma automação acessando o site ou não
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Desativer extensão
# O Selenium usa uma extensão junto com o Chromium para facilitar encontrar alguns elementos na página. Essa extensão deixa rastro e é uma das formas como sites vão verificar se é ou não um bot, então é necessário ser desativado
options.add_experimental_option("useAutomationExtension", False)


driver = webdriver.Chrome(service=service, options=options)


# Abaixo, listamos alguns objetos JavaScript o Selenuim deixa vazio ou preenchido de forma estranha e alteramos o valor deles para algo mais natural, que não será facilmente detectado
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
        Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
    """
})

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

time.sleep(2)

input("Esperar")