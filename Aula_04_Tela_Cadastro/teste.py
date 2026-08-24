import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_confirmacao = ()

    titulo = ft.Text("CADASTRO", font_family="comic sans", color="green", size=33, weight="Bold")

    nome = ft.TextField(
        label="Nome: ", 
        color="yellow",
        label_style=ft.TextStyle(font_family="Times new roman")
    )

    email = ft.TextField(
        label="Email: ", 
        color="yellow",
        label_style=ft.TextStyle(font_family="Times new roman")
    )

    botao_cadastrar = ft.Button("CADASTRAR", style= ft.ButtonStyle(
        shape = ft.RoundedRectangleBorder(radius=3),
        bgcolor={
            ft.ControlState.DEFAULT: "Blue", 
            ft.ControlState.HOVERED: "Dark_Blue" 
        },
        color= "White"
    ))

    page.add(titulo, nome, email, botao_cadastrar)

ft.run(main)
