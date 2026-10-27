from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Produto


def inicio(request):
    return HttpResponse("<h1>Olá, Django!</h1>")


def sobre(request):
    return HttpResponse(
        "<h1>Sobre</h1>"
        "<p>Disciplina: Programação III</p>"
        "<p>Equipe: Alisson</p>"
    )


def lista_produtos(request):
    dados = []
    for p in Produto.objects.all():
        dados.append({
            "codigo": p.codigo,
            "nome": p.nome,
            "preco": float(p.preco),
            "estoque": p.estoque,
        })
    return JsonResponse({"produtos": dados})


def produto(request, codigo):
    p = get_object_or_404(Produto, codigo=codigo)
    return JsonResponse({
        "codigo": p.codigo,
        "nome": p.nome,
        "preco": float(p.preco),
        "estoque": p.estoque,
    })

def produtos_disponiveis(request):
    dados = []
    for p in Produto.objects.filter(estoque__gt=0):
        dados.append({
            "codigo": p.codigo,
            "nome": p.nome,
            "preco": float(p.preco),
            "estoque": p.estoque,
        })
    return JsonResponse({"produtos": dados})