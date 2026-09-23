"""
servidor_local.py
API Local para Avaliação Prática - Programação III
Execução: python servidor_local.py
Dependências: Nenhuma (utiliza apenas a biblioteca padrão do Python)
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORTA = 8000

# Base de dados simulada em memória
PRODUTOS = {
    "101": {
        "codigo": "101",
        "nome": "Teclado Mecânico RGB",
        "categoria": "Periféricos",
        "preco": 250.00,
        "estoque": 14,
    },
    "102": {
        "codigo": "102",
        "nome": "Mouse Gamer 16000 DPI",
        "categoria": "Periféricos",
        "preco": 120.00,
        "estoque": 8,
    },
    "103": {
        "codigo": "103",
        "nome": "Monitor 24' Full HD 144Hz",
        "categoria": "Vídeo",
        "preco": 890.00,
        "estoque": 5,
    },
    "104": {
        "codigo": "104",
        "nome": "Headset USB 7.1",
        "categoria": "Áudio",
        "preco": 180.00,
        "estoque": 0,  # Item esgotado para testar validação de estoque
    },
}


class ApiHandler(BaseHTTPRequestHandler):

    def _enviar_json(self, status_code: int, dados: dict):
        corpo = json.dumps(dados, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        # Headers CORS para permitir requisições de qualquer origem/cliente
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(corpo)

    def do_GET(self):
        # Rota de consulta: /produto/<codigo>
        if self.path.startswith("/produto/"):
            codigo = self.path.replace("/produto/", "").strip()

            if codigo in PRODUTOS:
                self._enviar_json(200, PRODUTOS[codigo])
            else:
                self._enviar_json(
                    404,
                    {"erro": "Produto não localizado", "codigo_informado": codigo},
                )
            return

        # Rota raiz informativa para teste rápido no navegador
        if self.path in ("/", "/produto"):
            self._enviar_json(
                200,
                {
                    "mensagem": "API Local de Prova Online",
                    "exemplo_uso": f"http://localhost:{PORTA}/produto/101",
                    "codigos_disponiveis": list(PRODUTOS.keys()),
                },
            )
            return

        # Qualquer rota desconhecida
        self._enviar_json(400, {"erro": "Endpoint inválido"})

    def log_message(self, formato, *args):
        # Log simplificado no terminal para o aluno visualizar as chamadas recebidas
        print(f"[API Local] Requisição recebida: {self.command} {self.path} -> Status {args[1]}")


def main():
    servidor = HTTPServer(("localhost", PORTA), ApiHandler)
    print("=" * 65)
    print(f" Servidor da Avaliação ativo em: http://localhost:{PORTA}")
    print(" Exemplo para testar no navegador:")
    print(f" -> http://localhost:{PORTA}/produto/101")
    print(f" -> http://localhost:{PORTA}/produto/104 (Estoque zero)")
    print(" Pressione Ctrl + C no terminal para encerrar.")
    print("=" * 65)

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\n[API Local] Servidor encerrado com sucesso.")
        servidor.server_close()


if __name__ == "__main__":
    main()