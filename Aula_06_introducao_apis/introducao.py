import httpx

url = "https://viacep.com.br/ws/95219899/json/"
resp = httpx.get(url)

dados = resp.json()
print(dados)