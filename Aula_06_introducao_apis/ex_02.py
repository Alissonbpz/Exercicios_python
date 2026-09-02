import httpx

import flet as ft

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    cep = ft.TextField(label="CEP", value="")

    rua = ft.TextField(label="Logradouro", value="")
    bairro = ft.TextField(label="Bairro", value="")
    cidade = ft.TextField(label="Cidade", value="")
    sigla = ft.TextField(label="UF", value="")
    aviso = ft.Text("", size=12, color=ft.Colors.RED_600)
    
    def buscar_cep(e):
        cep_digitado = cep.value
        if cep_digitado and len(cep_digitado) == 8:
            url = f"https://viacep.com.br/ws/{cep_digitado}/json/"
            resp = httpx.get(url)
            dados = resp.json()

            rua.value = dados.get("logradouro", "")
            bairro.value = dados.get("bairro", "")
            cidade.value = dados.get("localidade", "")
            sigla.value = dados.get("uf", "")

            rua.update()
            bairro.update()
            cidade.update()
            sigla.update()
            aviso.value = ""
            aviso.update()
        else:
            aviso.value = "Por favor, digite um CEP válido."
            aviso.update()

    botao = ft.Button(content=ft.Text("Buscar"), on_click=buscar_cep)
    cep.on_submit = buscar_cep

    page.add(cep, rua, bairro, cidade, sigla, aviso, botao)


ft.run(main)