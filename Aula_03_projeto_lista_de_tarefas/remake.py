import flet as ft

def main(page: ft.Page):
    tarefa = ft.TextField(label="Digitar uma tarefa: ")
    lista_tarefas = ft.Column()
    def add_lista(e):
        lista_tarefas.controls.append(ft.Checkbox(label=tarefa.value))
        tarefa.value = ""
        page.update()
    botao_add = ft.IconButton(ft.Icons.ADD, on_click=add_lista)
    page.add(tarefa, botao_add, lista_tarefas)
ft.run(main)