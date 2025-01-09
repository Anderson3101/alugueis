from django.db import models
from alugueis.models import Aluguel

class ConsumoEnergia(models.Model):
    aluguel = models.OneToOneField(Aluguel, on_delete=models.CASCADE, related_name='consumo')
    leitura_anterior = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    leitura_atual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_kw = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    conta_celesc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.leitura_anterior and self.leitura_atual:
            consumo = self.leitura_atual - self.leitura_anterior
            self.valor_total = consumo * self.valor_kw
        elif self.conta_celesc:
            self.valor_total = self.conta_celesc
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Consumo: {self.valor_total or 0} - {self.aluguel.casa.nome}"

class Financeiro(models.Model):
    aluguel = models.OneToOneField(Aluguel, on_delete=models.CASCADE, related_name='financeiro')
    total_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pendente = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        consumo_total = self.aluguel.consumo.valor_total if self.aluguel.consumo else 0
        total_a_pagar = self.aluguel.valor_aluguel + consumo_total
        if self.total_pago < total_a_pagar:
            self.pendente = total_a_pagar - self.total_pago
        else:
            self.pendente = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pendência: {self.pendente or 0} - {self.aluguel.casa.nome}"
