from decimal import Decimal
from django.db import models
from casas.models import Casa
from despesas.models import Despesa
from alugueis.models import Aluguel

class Financeiro(models.Model):
    casa = models.ForeignKey('casas.Casa', on_delete=models.CASCADE, related_name='financeiro')
    total_despesas = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_alugueis = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_pago = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    pendencias = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Financeiro - {self.casa.nome}"

    def atualizar_valores(self):
        # Soma os valores das despesas relacionadas
        despesas = self.casa.despesas.all()
        total_despesas = sum(despesa.valor for despesa in despesas if despesa.valor)

        # Soma os valores dos aluguéis relacionados
        alugueis = self.casa.alugueis.all()
        total_alugueis = sum(aluguel.valor for aluguel in alugueis if aluguel.valor)

        # Atualiza os campos do modelo financeiro
        self.total_despesas = Decimal(total_despesas)
        self.total_alugueis = Decimal(total_alugueis)
        self.pendencias = self.total_despesas + self.total_alugueis - self.total_pago
        self.save()

    def registrar_pagamento(self, valor):
        # Garante que o valor seja Decimal
        valor = Decimal(valor)
        self.total_pago += valor
        self.pendencias -= valor
        if self.pendencias < Decimal('0.00'):
            self.pendencias = Decimal('0.00')
        self.save()
