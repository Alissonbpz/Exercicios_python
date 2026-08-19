import flet as ft

def main(page: ft.Page):
    page.title = "Prog III - Validação de Formulários"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Inputs e textos de feedback
    nome = ft.TextField(label="Nome", width=300)
    nome_erro = ft.Text("", size=12, color=ft.Colors.RED_600)

    email = ft.TextField(label="E-mail", width=300)
    email_erro = ft.Text("", size=12, color=ft.Colors.RED_600)

    msg_sucesso = ft.Text("", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_600)

    # 2. Evento do Botão
    def salvar(e):
        tem_erro = False

        # TODO: 1. Capturar e validar o campo 'nome'
        # - Verificar se possui no mínimo 3 caracteres
        # - Atualizar 'nome_erro.value' e a flag 'tem_erro'


        # TODO: 2. Capturar e validar o campo 'email'
        # - Verificar se possui '@' e '.' após o arroba
        # - Atualizar 'email_erro.value' e a flag 'tem_erro'


        # TODO: 3. Feedback final
        # - Se não houver erros: definir 'msg_sucesso.value' e limpar os inputs
        # - Se houver erros: limpar 'msg_sucesso.value'


        # TODO: 4. Chamar a atualização da tela
        page.update()

    # 3. Botão
    btn = ft.Button(
        content=ft.Text("Cadastrar"),
        on_click=salvar,
        width=300,
    )

    # 4. Montagem da interface
    page.add(
        ft.Text("Cadastro de Usuário", size=22, weight=ft.FontWeight.BOLD),
        nome,
        nome_erro,
        email,
        email_erro,
        btn,
        msg_sucesso,
    )

ft.run(main)