from django.db import models

class Despesa(models.Model):
    casa = models.ForeignKey('casas.Casa', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, choices=[('Energia', 'Energia'), ('Agua', 'Água')])
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_despesa = models.DateField()
    kw_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    kw_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.descricao == 'Energia' and self.kw_inicial is not None and self.kw_final is not None:
            consumo = self.kw_final - self.kw_inicial
            self.valor = consumo * 0.80  # R$ 0,80 por kW
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.descricao} - {self.casa.nome}"
