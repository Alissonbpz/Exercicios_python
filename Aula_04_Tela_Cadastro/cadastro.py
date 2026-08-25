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

        if senha.value == "" or len(senha.value) < 6:
            senha.error = "A senha precisa ter pelo menos 6 caracteres !!!"
            senha.update()
        else:
            senha.error = None
            senha.update()
        if selec_curso.value == None:
            selec_curso.error_text = "Selecione um curso!!!"
        else:
            selec_curso.error_text = None
            selec_curso.update()

        if not termos.value:
            termos.error = True
            termos.update()
        else:
            termos.error = None
            termos.update()

        
        if nome.error == None and email.error == None and senha.error == None and selec_curso.error_text == None and termos.error == None:
            nome.value = ""
            nome.update()

            email.value = ""
            email.update()

            senha.value = ""
            senha.update()

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

    senha = ft.TextField(
        label="Senha: ", 
        color="yellow",
        label_style=ft.TextStyle(font_family="Times new roman"),
        border_color="white",
        focused_border_color = "blue900",
        password=True,
        can_reveal_password=True
    )

    selec_curso = ft.Dropdown(
        label="Curso",
        options=[
            ft.dropdown.Option("Sistemas de Informação"),
            ft.dropdown.Option("Ciência da Computação"),
            ft.dropdown.Option("Engenharia de Software"),
        ]
    )

    termos = ft.Checkbox(label="Termos de aceite", label_style=ft.TextStyle(font_family="Times new roman"))

    linha = ft.Row(
    controls=[termos],
    alignment=ft.MainAxisAlignment.CENTER,   # AQUI é onde entra o alignment
    )
    
    botao_cadastrar = ft.Button("CADASTRAR", on_click=cadastrar, style= ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius=3),
        bgcolor={
            ft.ControlState.DEFAULT: "Blue", 
            ft.ControlState.HOVERED: "Dark_Blue" 
        },
        color= "White"
    ))

    page.add(titulo, nome, email, senha, selec_curso, linha, txt_confirmacao, botao_cadastrar)

ft.run(main)
