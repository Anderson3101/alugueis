from django.db import models
from casas.models import Casa

class Despesa(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='despesas')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_despesa = models.DateField()
    
    def __str__(self):
        return f"{self.descricao} - {self.casa.nome} - R$ {self.valor}"
