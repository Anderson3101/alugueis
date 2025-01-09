from django.shortcuts import render
from .models import Financeiro

def detalhes_financeiros(request):
    financeiros = Financeiro.objects.all()
    return render(request, 'financeiro/detalhes_financeiros.html', {'financeiros': financeiros})
