from django.http import HttpResponse, Http404, JsonResponse

PRODUTOS = {
    101: {
        "codigo": "101",
        "nome": "Teclado Mecânico RGB",
        "categoria": "Periféricos",
        "preco": 250.00,
        "estoque": 14,
    },
    102: {
        "codigo": "102",
        "nome": "Mouse Gamer 16000 DPI",
        "categoria": "Periféricos",
        "preco": 120.00,
        "estoque": 8,
    },
    103: {
        "codigo": "103",
        "nome": "Monitor 24' Full HD 144Hz",
        "categoria": "Vídeo",
        "preco": 890.00,
        "estoque": 5,
    },
    104: {
        "codigo": "104",
        "nome": "Headset USB 7.1",
        "categoria": "Áudio",
        "preco": 180.00,
        "estoque": 0,
    },
}

def inicio(request):
    return HttpResponse("<h1>Olá, Django!</h1>")

def sobre(request):
    return HttpResponse(
        "<h1>Sobre</h1>"
        "<p>Disciplina: Programação III</p>"
        "<p>Equipe: Alisson</p>"
    )

def produtos(request):
    return JsonResponse({"produtos": list(PRODUTOS.values())})

def produto(request, codigo):
    if codigo not in PRODUTOS:
        raise Http404("Produto não encontrado")
    return JsonResponse(PRODUTOS[codigo])