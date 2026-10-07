from django.shortcuts import render

from django.http import Http404, JsonResponse

PRODUTOS = {
    101: {"nome":"Teclado Mecânico", "preco":120.0},
    102:{"nome":"Mouse Gamer","preco":120.0},
}

def produto(request,codigo):
    if codigo not in PRODUTOS:
        raise Http404("Produto não encontrado")
    return JsonResponse(PRODUTOS[codigo])