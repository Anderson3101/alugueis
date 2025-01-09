from django import forms
from .models import Casa

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['nome', 'endereco']
