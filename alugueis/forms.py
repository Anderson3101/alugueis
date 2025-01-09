from django import forms
from .models import Aluguel

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['casa', 'mes_referencia', 'valor_aluguel', 'pago']
        widgets = {
            'mes_referencia': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valor_aluguel': forms.TextInput(attrs={'class': 'form-control'}),
            'casa': forms.Select(attrs={'class': 'form-control'}),
            'pago': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
