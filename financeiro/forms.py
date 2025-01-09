from django import forms
from .models import ConsumoEnergia

class ConsumoEnergiaForm(forms.ModelForm):
    class Meta:
        model = ConsumoEnergia
        fields = ['aluguel', 'leitura_anterior', 'leitura_atual', 'valor_kw', 'conta_celesc']
