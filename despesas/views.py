from django.shortcuts import render, get_object_or_404, redirect
from .models import Despesa
from .forms import DespesaForm

def listar_despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'despesas/listar_despesas.html', {'despesas': despesas})

def cadastrar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm()
    return render(request, 'despesas/cadastrar_despesa.html', {'form': form})

def editar_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm(instance=despesa)
    return render(request, 'despesas/editar_despesa.html', {'form': form})

def excluir_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)
    if request.method == 'POST':
        despesa.delete()
        return redirect('listar_despesas')
    return render(request, 'despesas/excluir_despesa.html', {'despesa': despesa})
