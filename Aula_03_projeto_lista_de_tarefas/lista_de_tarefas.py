import flet as ft

def main(page: ft.page):

    tarefa = ft.TextField(label="Digite uma tarefa:")

    botao_add = ft.IconButton(ft.Icons.ADD)

    page.add(tarefa,botao_add)

ft.app(target=main)