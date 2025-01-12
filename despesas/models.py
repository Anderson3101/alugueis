from django.db import models
from casas.models import Casa

class Despesa(models.Model):
    casa = models.ForeignKey('casas.Casa', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, choices=[('Energia', 'Energia'), ('Água', 'Água')])
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    kw_inicial = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    kw_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    data_despesa = models.DateField()

    def __str__(self):
        return f"{self.descricao} - {self.casa}"
