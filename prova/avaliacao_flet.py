import flet as ft
import httpx
def main(page:ft.Page):
    page.title = "Prova"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    codigo = ft.TextField(label="Digite o codigo do produto: ", value="", width=333, color= "blue")
    nome = ft.Text("")
    categoria = ft.Text("")
    preco = ft.Text("")
    cm_desconto = ft.Text("")
    aviso = ft.Text("", size=12, color=ft.Colors.RED_600)

    def processando(e):
        codigo_digitado = codigo.value.strip()
        if codigo_digitado != "":
            cd = int(codigo_digitado)
        if codigo_digitado and len(codigo_digitado) == 3:
            if cd <= 100 or cd >=105:
                aviso.value = "Este codigo não existe!!!"
                codigo.value =""
                nome.value =""
                categoria.value = ""
                preco.value = ""
                cm_desconto.value = ""
                page.update()
                return
            url = f"http://localhost:8000/produto/{codigo_digitado}"
            resp = httpx.get(url)
            dados = resp.json()
            estoque = dados.get("estoque","")
            quant =int(estoque)
            if quant == 0:
                aviso.value = "Produto esgotado no estoque!!!"
                codigo.value =""
                nome.value =""
                categoria.value = ""
                preco.value = ""
                cm_desconto.value = ""
                page.update()
                return
            nome.value = f"Nome do produto: {dados.get("nome", "")}"
            categoria.value = f"Categoria: {dados.get("categoria","")}"
            valor = float(dados.get("preco",{}))
            preco.value = f"Valor original: {valor:.2f}R$"
            cm_desconto.value = f"Valor com desconto (pagamento avista): {valor*0.90:.2f}R$"
            aviso.value = ""
            page.update()
        else:
            aviso.value = "             O codigo digitado é ivalido!!!\nPor favor, digite um codigo de produto valido."
            codigo.value =""
            nome.value =""
            categoria.value = ""
            preco.value = ""
            cm_desconto.value = ""
            page.update()

    mostrar = ft.Column(controls =[nome, categoria,preco,cm_desconto])
    botao = ft.Button("Buscar", width=333, on_click=processando)
    codigo.on_submit = processando

    page.add(codigo, mostrar, botao, aviso)
ft.run(main)