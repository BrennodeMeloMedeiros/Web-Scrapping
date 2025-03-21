# Objetivo

O objetivo dessa automação é coletar dados e oportunidades de emprego que o linkedin atribue ao seu perfil de forma rápida e simplificado.

A prioridade desse projeto é ser um Web Scrapper indetectável que oferece conveniência ao usuário. Tornam essa Scrapper indetável:
- Utilização de Cookies para login único;
- Simulação de comportamento humano randomizado;
- Configuração do Chromium para eliminar rastros e deteções via JavaScript.

# Passo 1 - Usando Selenium (com Chrome)
Vamos instalar o selenium:
 - pip install selenium 
 e vamos instalar o webdriver:
 - pip install selenium webdriver-manager

O WebDriver é obrigatório para a utilização do Selenium, mas ele não é instalado automaticamente. Se necessário, é possível realizar a instalação manualmente, mas nesse projeto optei pela instalação automática via pip.

# Passo 2 - Configuração de conta Linkedin

Serão necessário três dados: email e senha do seu Linkedin e agent do seu navegador.

Como pegar o AGENT do seu navegador:
- Acesse https://www.whatismybrowser.com/
- Desça até o fim da página, onde seu AGENT pode ser encontrado. Ele parece com algo assim: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Chrome/134.0.5827.94 Edg/134.0 Safari/537.88"

Por fim, renomeie o arquivo "credential.json.example" para "credential.json".
