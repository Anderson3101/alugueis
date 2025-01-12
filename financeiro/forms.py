class ConsumoEnergiaForm(forms.ModelForm):
    class Meta:
        model = ConsumoEnergia
        fields = ['aluguel', 'leitura_anterior', 'leitura_atual', 'valor_kw', 'conta_celesc']
        widgets = {
            'leitura_anterior': forms.NumberInput(attrs={'class': 'form-control'}),
            'leitura_atual': forms.NumberInput(attrs={'class': 'form-control'}),
        }
