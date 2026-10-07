from django.urls import path
from . import views

urlpatterns = [
    path("produtos/<int:codigo>/",
         views.produto,
         name="produto"),
]