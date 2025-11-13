from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=0)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome
