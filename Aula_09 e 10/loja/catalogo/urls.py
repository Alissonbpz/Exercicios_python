from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("sobre/", views.sobre, name="sobre"),
    path("produtos/", views.lista_produtos, name="produtos"),
    path("produtos/<int:codigo>/", views.produto, name="produto"),
    path("produtos/disponiveis/", views.produtos_disponiveis, name="produtos_disponiveis"),
]