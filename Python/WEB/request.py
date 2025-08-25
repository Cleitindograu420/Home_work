import requests

resposta = requests.get("https://httpbin.org/html")
print(resposta.content)