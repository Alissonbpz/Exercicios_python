import flet as ft

def main(page:ft.Page):
    page.title = "Treinando exercicio usando flet"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment =ft.CrossAxisAlignment.CENTER

    cabecalho = ft.Text("Cadastro", weight="bold", size=50, color="blue")

    txt_confirmacao = ft.Text("", size= 18,color="green")

    def validacao(e):
        if nome.value == "" or len(nome.value)<3:
            nome.error="Nome invalido, minimo de 3 caracteres!!!"
            nome.update()
        else:
            nome.error = None
            nome.update()
        if email.value == "" or "@" not in email.value:
            email.error = "Email invalido!!!"
            email.update()
        else:
            email.error = None
            email.update()
        if nome.error == None and email.error == None:
            txt_confirmacao.value = "Cadastro realizado!"
            txt_confirmacao.update()
            nome.value = ""
            email.value = ""
            nome.update()
            email.update()

    nome = ft.TextField(label="Digite seu nome: ", color ="yellow")
    email= ft.TextField(label="Email: ", color ="yellow")
    botao_cadastrar = ft.Button("Cadastrar", on_click=validacao)

    page.add(cabecalho,nome,email,txt_confirmacao,botao_cadastrar)

ft.run(main)