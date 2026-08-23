import flet as ft

import asyncio

def main(page: ft.Page):
    page.title = "Cadastro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    msg_sucesso = ft.Text("", color="green", size=20, font_family="open sans")

    async def cadastrar(e):
        if nome.value == "" or len(nome.value) < 3 :
            nome.error = "O nome precisa ter pelo menos 3 letras!!!"
        else:
            nome.error = None
        nome.update()
        if email.value == "" or "@" not in email.value:
            email.error = "Digite um email válido com '@'!!!"
        else:
            email.error = None
        email.update()
        if nome.error == None and email.error == None:
            msg_sucesso.value = "Cadastro realizado com sucesso!!!"
            msg_sucesso.update()
            nome.value = ""
            nome.update()
            email.value = ""
            email.update()
            await asyncio.sleep(3)
            msg_sucesso.value = ""
            msg_sucesso.update()

    titulo = ft.Text("CADASTRO", size=40, color="gray", weight="bold",font_family="Arial")

    nome = ft.TextField(label="Digite seu nome: ", color="yellow", text_size=12, label_style=ft.TextStyle( color= "white"))

    email = ft.TextField(label="Email: ", color="yellow", text_size=12, label_style= ft.TextStyle(color="white"))

    botao = ft.Button(
        "Cadastrar", color="white",
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: "blue",
                ft.ControlState.HOVERED: "blue900",
            },
            shape = ft.RoundedRectangleBorder(radius=2),
            text_style= ft.TextStyle(font_family="Times new roman", size=20)
        ), on_click= cadastrar
    )

    page.add(titulo, nome, email, msg_sucesso, botao)

ft.run(main)