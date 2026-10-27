from django.db import models

class Produto(models.Model):
    codigo = models.PositiveIntegerField(unique=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome