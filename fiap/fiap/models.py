from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    data_fabricacao = models.DateTimeField('data de fabricacao')

