from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=255)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
