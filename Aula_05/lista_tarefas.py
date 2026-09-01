import flet as ft

def main(page: ft.Page):
    page.title = "Prog III - Lista de Tarefas Dinâmica"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    item_input = ft.TextField(label="Nova Tarefa", width=320)
    categoria_item = ft.TextField(label="Categoria: ", width=320)
    msg_erro = ft.Text("", size=12, color=ft.Colors.RED_600)

    lista_view = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)

    quant_tarefas = ft.Text(f"Tarefas pendentes: {len(lista_view.controls)}")

    def atualizar_contador():
        total = len(lista_view.controls)
        concluidas = sum(1 for card in lista_view.controls if card.content.leading.value)
        pendentes = total - concluidas
        quant_tarefas.value = f"Tarefas pendentes: {pendentes}"
        quant_tarefas.update()

    def remover_tarefa(card_alvo):
        if card_alvo in lista_view.controls:
            lista_view.controls.remove(card_alvo)
            page.update()
            atualizar_contador()

    def adicionar_tarefa(e):
        texto = (item_input.value or "").strip()

        if texto == "":
            msg_erro.value = "Campo de tarefa obrigatório!"
            page.update()
            return
        else:
            msg_erro.value = ""
            page.update()

        titulo_tarefa = ft.Text(texto, weight=ft.FontWeight.BOLD)

        def marcar_concluida(e):
            if checkbox.value:
                titulo_tarefa.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH, color=ft.Colors.GREEN_600)
            else:
                titulo_tarefa.style = None
            titulo_tarefa.update()
            atualizar_contador()

        checkbox = ft.Checkbox(on_change=marcar_concluida)

        novo_card = ft.Card(
            content=ft.ListTile(
                leading=checkbox,
                title=titulo_tarefa,
                subtitle=ft.Text(categoria_item.value, weight=ft.FontWeight.BOLD),
                trailing=ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=ft.Colors.RED_600,
                    on_click=lambda _: remover_tarefa(novo_card)
                )
            )
        )

        lista_view.controls.append(novo_card)
        item_input.value = ""
        categoria_item.value = ""
        atualizar_contador()
        page.update()

    item_input.on_submit = adicionar_tarefa

    btn_add = ft.Button(
        content=ft.Text("Adicionar Tarefa"),
        on_click=adicionar_tarefa,
        width=320,
    )

    def excluir_tarefas(e):
        lista_view.controls.clear()
        atualizar_contador()
        page.update()

    btn_del = ft.Button(
        content=ft.Text("Deletar tarefas"),
        on_click=excluir_tarefas,
        width=150,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=3),
            bgcolor="red"
        ),
        color="white"
    )

    container_lista = ft.Container(
        content=lista_view,
        width=380,
        height=320,
        border=ft.Border.all(1, ft.Colors.GREY_400),
        border_radius=8,
    )

    rodape = ft.Row(
        controls=[quant_tarefas, btn_del], spacing=50,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Text("Minhas Tarefas", size=22, weight=ft.FontWeight.BOLD),
        item_input,
        categoria_item,
        msg_erro,
        btn_add,
        ft.Divider(),
        container_lista,
        rodape
    )

ft.run(main)