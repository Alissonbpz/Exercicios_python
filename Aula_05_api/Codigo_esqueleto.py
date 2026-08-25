import flet as ft

def main(page: ft.Page):
    page.title = "Prog III - Lista de Tarefas Dinâmica"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Entrada de dados e mensagem de erro
    item_input = ft.TextField(label="Nova Tarefa", width=320)
    msg_erro = ft.Text("", size=12, color=ft.Colors.RED_600)

    # 2. Lista com rolagem gerenciada
    lista_view = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)

    # TODO 1: Implementar a remoção do item específico
    def remover_tarefa(card_alvo):
        # 1. Remover 'card_alvo' da lista 'lista_view.controls'
        # 2. Atualizar a página com page.update()
        pass

    # TODO 2: Implementar a criação e inserção dinâmica
    def adicionar_tarefa(e):
        texto = (item_input.value or "").strip()

        # 1. Validar se 'texto' está vazio:
        #    - Se vazio: definir 'msg_erro.value' e atualizar a página.
        #    - Se válido: limpar 'msg_erro.value'.

        # 2. Instanciar um ft.Card contendo um ft.ListTile:
        #    - leading: ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE)
        #    - title: ft.Text(texto, weight=ft.FontWeight.BOLD)
        #    - trailing: ft.IconButton(
        #          icon=ft.Icons.DELETE, 
        #          icon_color=ft.Colors.RED_600,
        #          on_click=lambda _: remover_tarefa(novo_card)
        #      )

        # 3. Adicionar 'novo_card' em 'lista_view.controls'
        # 4. Limpar o valor de 'item_input'
        # 5. Atualizar a página com page.update()
        pass

    # Atalho para cadastrar teclando Enter
    item_input.on_submit = adicionar_tarefa

    # Botão de adicionar
    btn_add = ft.Button(
        content=ft.Text("Adicionar Tarefa"),
        on_click=adicionar_tarefa,
        width=320,
    )

    # Área visual delimitada para a lista
    container_lista = ft.Container(
        content=lista_view,
        width=380,
        height=320,
        border=ft.Border.all(1, ft.Colors.GREY_400),
        border_radius=8,
    )

    # 3. Montagem da Interface
    page.add(
        ft.Text("Minhas Tarefas", size=22, weight=ft.FontWeight.BOLD),
        item_input,
        msg_erro,
        btn_add,
        ft.Divider(),
        container_lista,
    )

ft.run(main)