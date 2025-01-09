from django import forms
from .models import Despesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['casa', 'descricao', 'valor', 'data_despesa']
        widgets = {
            'casa': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_despesa': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
