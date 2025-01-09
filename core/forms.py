from django import forms
from .models import Casa, Aluguel, ConsumoEnergia

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['nome', 'endereco']

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['casa', 'mes_referencia', 'valor_aluguel', 'pago']

class ConsumoEnergiaForm(forms.ModelForm):
    class Meta:
        model = ConsumoEnergia
        fields = ['aluguel', 'leitura_anterior', 'leitura_atual', 'valor_kw']
