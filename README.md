# Objetivo
O objetivo dessa automação é coletar dados e oportunidades de emprego que o linkedin atribue ao seu perfil de forma rápida e simplificado.

A prioridade desse projeto é ser um Web Scrapper indetectável que oferece conveniência ao usuário. Tornam essa Scrapper indetável:
- Utilização de Cookies para login único;
- Simulação de comportamento humano randomizado (moviemnto de cursor, pausa nas ações, etc);
- Configuração do Chromium para eliminar rastros e deteções via JavaScript.

# Passo 1 - Usando Selenium (com Chrome)
Vamos instalar o selenium:
 - pip install selenium 
 e vamos instalar o webdriver:
 - pip install selenium webdriver-manager

O WebDriver é obrigatório para a utilização do Selenium, mas ele não é instalado automaticamente. Se necessário, é possível realizar a instalação manualmente, mas nesse projeto optei pela instalação automática via pip.

# Passo 2 - Configuração de USER AGENT
O USER AGENT é uma string utilizada por sites para identificar algumas informações básicas do seu navegador. Ao utilizar o Selenium, esse string é 
substituida por uma string genérica, o que é um indicativo que um automação está sendo utilizada para acessar a conta. Para evitar problemas de 
banimento ou suspenção, é necessário que o você atualize o variavel "USER_AGENT", no arquivo [main.py] ante de executar a automação. 

Como pegar o USER AGENT do seu navegador:
- Acesse https://www.whatismybrowser.com/
- Desça até o fim da página, onde seu AGENT pode ser encontrado. Ele parece com algo assim: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Chrome/134.0.5827.94 Edg/134.0 Safari/537.88"

# Passo 3 - Rodar [primeiro_acesso.py]
É necessário que o login para a sua conta seja realizada manualmente pelo menos uma vez.

Rode o script [priimeiros_acesso.py]. Ele irá abrir a página de login do linkedin. Você terá 30 segundos antes da automação fechar automaticamente e salvar os cookies. Utilize esses segundos para realizar o login na sua conta e resolver o CAPTCHA, se necessário. 

! - Se os 30 segundos não foram o suficiente, tente novamente. Os cookies da última tentativa são os que valem.