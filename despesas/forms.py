from django import forms
from .models import Despesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['casa', 'descricao', 'kw_inicial', 'kw_final', 'valor', 'data_despesa']
        widgets = {
            'kw_inicial': forms.NumberInput(attrs={'step': '0.01'}),
            'kw_final': forms.NumberInput(attrs={'step': '0.01'}),
            'valor': forms.NumberInput(attrs={'readonly': True, 'step': '0.01'}),
        }

def clean(self):
    cleaned_data = super().clean()
    descricao = cleaned_data.get('descricao')
    kw_inicial = cleaned_data.get('kw_inicial')
    kw_final = cleaned_data.get('kw_final')

    if descricao == "Energia":
        if kw_inicial is None or kw_final is None:
            raise forms.ValidationError("kW Inicial e kW Final são obrigatórios para despesas de Energia.")
        if kw_final < kw_inicial:
            raise forms.ValidationError("kW Final deve ser maior ou igual a kW Inicial.")
    return cleaned_data
