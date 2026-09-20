import httpx
import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    valor = ft.TextField(label="Informe o valor em Reais (R$): ", color = "blue", width=320, label_style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD, color="green"))

    v_USD = ft.Text("")
    v_EUR = ft.Text("")
    v_BTC = ft.Text("")

    valores = ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                controls=[v_USD, v_EUR, v_BTC]
            )
        )
    )

    aviso = ft.Text("", color="red")

    def convert(e):
        texto_valor = (valor.value or "").strip().replace(",", ".")

        if texto_valor == "":
            aviso.value = "Por favor, digite um valor."
            v_USD.value = ""
            v_EUR.value = ""
            v_BTC.value = ""
            v_USD.update()
            v_EUR.update()
            v_BTC.update()
            aviso.update()
            return

        try:
            valor_digitado = float(texto_valor)
        except ValueError:
            aviso.value = "Digite apenas números válidos."
            v_USD.value = ""
            v_EUR.value = ""
            v_BTC.value = ""
            v_USD.update()
            v_EUR.update()
            v_BTC.update()
            aviso.update()
            return

        if valor_digitado <= 0:
            aviso.value = "Por favor, digite um valor maior que zero."
            aviso.update()
            v_USD.value = ""
            v_EUR.value = ""
            v_BTC.value = ""
            v_USD.update()
            v_EUR.update()
            v_BTC.update()
            return

        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

        
        resp = httpx.get(url)

        dados = resp.json()
        

        cotacao_usd = float(dados.get("USDBRL", {}).get("bid", 0))
        cotacao_eur = float(dados.get("EURBRL", {}).get("bid", 0))
        cotacao_btc = float(dados.get("BTCBRL", {}).get("bid", 0))

        resultado_usd = valor_digitado / cotacao_usd
        resultado_eur = valor_digitado / cotacao_eur
        resultado_btc = valor_digitado / cotacao_btc

        v_USD.value = f"USD: {resultado_usd:.2f} (cotação: {cotacao_usd:.2f})"
        v_EUR.value = f"EUR: {resultado_eur:.2f} (cotação: {cotacao_eur:.2f})"
        v_BTC.value = f"BTC: {resultado_btc:.6f} (cotação: {cotacao_btc:.2f})"

        v_USD.update()
        v_EUR.update()
        v_BTC.update()

        aviso.value = ""
        aviso.update()

    botao = ft.Button(content=ft.Text("Converter"), on_click=convert)
    valor.on_submit = convert

    page.add(valor, botao, valores, aviso)

ft.run(main)