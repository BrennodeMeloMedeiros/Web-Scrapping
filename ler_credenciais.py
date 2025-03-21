import json

with open("./credentials.json", "r") as credentialsFile:
    credenciais =   json.load(credentialsFile)

emailLinkedin = credenciais["EMAIL"]
senhaLinkedin = credenciais["SENHA"]
userAgentNavegador = credenciais["AGENT"]