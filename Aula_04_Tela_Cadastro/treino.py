import flet as ft

def main(page:ft.Page):
    page.title = "Treinando exercicio usando flet"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment =ft.CrossAxisAlignment.CENTER

    cabecalho = ft.Text("Cadastro", weight="bold", size=50, color="blue")

    txt_confirmacao = ft.Text("", size= 30,color="green",weight="bold")

    def validacao(e):
        if nome == "" or len(nome.value):
            nome.error="Nome invalido, minimo de 3 caracteres."
        nome.update()

    nome = ft.TextField(label="Digite seu nome: ", color ="yellow")
    email= ft.TextField(label="Email: ", color ="yellow")
    botao_cadastrar = ft.Button("Cadastrar", on_click=validacao)

    page.add(cabecalho,nome,email,txt_confirmacao,botao_cadastrar)

ft.run(main)