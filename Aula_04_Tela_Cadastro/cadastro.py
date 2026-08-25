import flet as ft
import asyncio
def main(page: ft.Page):
    page.title = "Cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_confirmacao = ft.Text("", color="green")

    async def cadastrar(e):
        if nome.value == "" or len(nome.value) < 3 :
            nome.error = "O nome precisa ter pelo menos 3 letras !!!"
            nome.update()
        else:
            nome.error = None
            nome.update()
        if email.value == "" or "@" not in email.value:
            email.error = "Digite um email válido com '@'!!!"
            email.update()
        else:
            email.error = None
            email.update()
        if nome.error == None and email.error == None:
            nome.value = ""
            nome.update()

            email.value = ""
            email.update()

            txt_confirmacao.value = "Cadastro realizado com sucesso!!!"
            txt_confirmacao.update()

            await asyncio.sleep(3)

            txt_confirmacao.value = ""
            txt_confirmacao.update()
            

    titulo = ft.Text("CADASTRO", font_family="comic sans", color="green", size=33, weight="Bold")

    nome = ft.TextField(
        label="Nome: ", 
        color="yellow",
        label_style=ft.TextStyle(font_family="Times new roman"),
        border_color="white",
        focused_border_color = "blue900"
    )

    email = ft.TextField(
        label="Email: ", 
        color="yellow",
        label_style=ft.TextStyle(font_family="Times new roman"),
        border_color="white",
        focused_border_color = "blue900"
    )

    botao_cadastrar = ft.Button("CADASTRAR", on_click=cadastrar, style= ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius=3),
        bgcolor={
            ft.ControlState.DEFAULT: "Blue", 
            ft.ControlState.HOVERED: "Dark_Blue" 
        },
        color= "White"
    ))

    page.add(titulo, nome, email, txt_confirmacao, botao_cadastrar)

ft.run(main)
