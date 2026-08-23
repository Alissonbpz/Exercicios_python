import flet as ft

def main(page:ft.Page):
    page.title = "Cadastro"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("CADASTRO", size=33, color="blue")

    nome = ft.TextField(label="Digite seu nome: ", color="yellow", text_size=15)

    email = ft.TextField(label="Email: ", color="yellow", text_size=15)

    botao = ft.Button = ("Cadastrar")

    page.add(titulo, nome, email, botao)


ft.run(main)