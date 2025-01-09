from django.db import models
from casas.models import Casa

class Aluguel(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='alugueis')
    mes_referencia = models.DateField()
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.casa.nome} - {self.mes_referencia.strftime('%m/%Y')}"
