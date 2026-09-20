import flet as ft

def main(page:ft.Page):
    page.title = "Tela de cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    texto_confirm = ft.Text("", color="green")

    def confirmacao(e):
        if nome.value == "" or len(nome.value)< 3:
            nome.error = "O nome deve ter no minimo 3 caracteres"
            nome.update()
        else:
            nome.value = ""
            nome.error = None
            nome.update()
        if email.value == "" or "@" not in email.value:
            email.error = "O email deve ter @!!!"
            email.update()
        else:
            email.value =""
            email.error =None
            email.update()
        if nome.error == None and email.error == None:
            texto_confirm.value = "Cadastro realizado!!!"
            texto_confirm.update()


    titulo = ft.Text("Cadastro de usuario", size=28, font_family="Comic sans",weight="bold",color="green")
    nome = ft.TextField(
        label="Nome:",
        color ="yellow",
        border_color= "grey",
        label_style=ft.TextStyle(font_family="Times new roman"),
        focused_border_color = "blue900"
    )
    email = ft.TextField(
        label="Email:",
        color ="yellow",
        border_color= "grey",
        label_style=ft.TextStyle(font_family="Times new roman"),
        focused_border_color = "blue1500"
    )
    botao_cadastro =ft.Button("Cadastrar",on_click= confirmacao)
    page.add(titulo,nome,email,texto_confirm,botao_cadastro)
ft.run(main)