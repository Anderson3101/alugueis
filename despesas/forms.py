from django import forms
from .models import Despesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['casa', 'descricao', 'kw_inicial', 'kw_final', 'valor', 'data_despesa']
        widgets = {
            'data_despesa': forms.DateInput(attrs={'type': 'date'}),
        }
