from django.db import models
from produtos.models import Produto

class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='movimentacoes_estoque')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.title()} - {self.produto.nome} ({self.quantidade})"
