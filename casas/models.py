from django.db import models

class Casa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
