from django.db import models
from produtos.models import Produto
from usuarios.models import Usuario

class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    data = models.DateField()
    observacao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} ({self.quantidade})"
