from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Financeiro
from despesas.models import Despesa
from alugueis.models import Aluguel

@receiver(post_save, sender=Despesa)
def atualizar_financeiro_despesa(sender, instance, **kwargs):
    financeiro, created = Financeiro.objects.get_or_create(casa=instance.casa)
    financeiro.atualizar_valores()

@receiver(post_save, sender=Aluguel)
def atualizar_financeiro_aluguel(sender, instance, **kwargs):
    financeiro, created = Financeiro.objects.get_or_create(casa=instance.casa)
    financeiro.atualizar_valores()
