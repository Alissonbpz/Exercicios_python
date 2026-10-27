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
            nome.error = None
            nome.update()
        if email.value == "" or "@" not in email.value:
            email.error = "O email deve ter @!!!"
            email.update()
        else:
            email.error =None
            email.update()
        if senha.value == "" or len(senha.value) < 6:
            senha.error = "A senha deve ter no minimo 6 caracteres"
            senha.update()
        else:
            senha.error =None
            senha.update()
        if curso.value == None:
            curso.error_text = "Selecione um curso!!!"
            curso.update()
        else:
            curso.error_text = None
            curso.update()
        if not termos.value:
            termos.error = True
            termos.update()
        else:
            termos.error = False
            termos.update()
        if nome.error == None and email.error == None and senha.error == None and curso.error_text == None and termos.error == False:
            texto_confirm.value = "Cadastro realizado!!!"
            nome.value = ""
            nome.update()
            email.value = ""
            email.update()
            senha.value = ""
            senha.update()
            curso.value = None
            curso.update()
            termos.value = False
            termos.update()
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
    senha = ft.TextField(
        label="Senha:",
        color ="yellow",
        border_color= "grey",
        label_style=ft.TextStyle(font_family="Times new roman"),
        focused_border_color = "blue1500",
        password=True
    )
    curso = ft.Dropdown(
        label="Selecao de curso",
        options=[
            ft.dropdown.Option("Sistemas de Informação"),
            ft.dropdown.Option("Ciencia da Computacao"),
            ft.dropdown.Option("Analise e desenvolvimento de si")
            ])
    termos=ft.Checkbox(label="Aceitar termos")
    linha = ft.Row(controls=[termos],alignment=ft.MainAxisAlignment.CENTER)

    def reset_fields(e):
        nome.value = ""
        nome.error= None
        nome.update()
        email.value = ""
        email.error=None
        email.update()
        senha.value = ""
        senha.error=None
        senha.update()
        curso.value = None
        curso.error_text= None
        curso.update()
        termos.value = False
        termos.error=False
        termos.update()
        texto_confirm.update()
        
    reset = ft.Button("Reset",on_click=reset_fields)
    
    botao_cadastro =ft.Button("Cadastrar",on_click= confirmacao)
    page.add(titulo,nome,email,senha,curso,linha,texto_confirm,botao_cadastro,reset)
ft.run(main)