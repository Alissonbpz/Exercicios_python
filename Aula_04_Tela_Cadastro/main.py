import flet as ft
import asyncio

def main(page: ft.Page):
    page.title = "Página de Cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    cabeçalho = ft.Text("CADASTRO", size=30, weight="bold", color="blue")

    nome = ft.TextField(label="Digite seu nome: ")

    email = ft.TextField(label="Email: ")

    d_certo = ft.Text("", color="green")
    
    async def validar_cadastro(e):
        if nome.value.strip() == "" or len(nome.value.strip()) < 3:
            nome.error = "O nome precisa ter pelo menos 3 letras."
        else:
            nome.error = None
        nome.update() 
        
        if email.value.strip() == "" or "@" not in email.value:
            email.error = "Digite um e-mail válido com '@'."
        else:
            email.error= None
        email.update() 

        if nome.error is None and email.error is None:
            d_certo.value = f"Cadastro realizado com sucesso, {nome.value}!"
            nome.value = ""
            email.value = ""
            await asyncio.sleep(3)
            d_certo.value = ""
        nome.update()
        email.update()
        d_certo.update()
    botao_cadastro = ft.Button("Cadastrar", on_click=validar_cadastro)
    
    page.add(cabeçalho, nome, email, d_certo, botao_cadastro)

ft.run(main)