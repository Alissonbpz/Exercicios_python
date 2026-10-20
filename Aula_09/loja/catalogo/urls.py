from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("produtos/<int:codigo>/", views.produto, name="produto"),
]