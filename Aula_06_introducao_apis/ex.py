import httpx

import flet as ft

url = "https://viacep.com.br/ws/95219899/json/"
resp = httpx.get(url)
dados = resp.json()
def main(page: ft.Page):

    cep = ft.TextField(label="CEP", value=dados.get("cep", ""))
    rua = ft.TextField(label="Logradouro", value=dados.get("logradouro", ""))
    bairro = ft.TextField(label="Bairro", value=dados.get("bairro", ""))
    cidade = ft.TextField(label="Cidade", value=dados.get("localidade", ""))
    sigla = ft.TextField(label="UF", value=dados.get("uf", ""))

    page.add(cep, rua, bairro, cidade, sigla)


ft.run(main)