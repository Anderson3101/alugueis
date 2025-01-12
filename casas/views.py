from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Casa
from .forms import CasaForm

def listar_casas(request):
    casas = Casa.objects.all()
    return render(request, 'casas/listar_casas.html', {'casas': casas})

def cadastrar_casa(request):
    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Casa cadastrada com sucesso!')
            return redirect('listar_casas')
        else:
            message.error(request, 'Erro ao cadastrar a casa. Verifique os dados e tente novamente.')
    else:
        form = CasaForm()
    return render(request, 'casas/cadastrar_casa.html', {'form': form})

def excluir_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if request.method == 'POST':
        casa.delete()
        messages.success(request, 'Casa excluida com sucesso!')
        return redirect('listar_casas')

def editar_casa(request, pk):
    casa = get_object_or_404(Casa, pk=pk)
    if request.method == 'POST':
        form = CasaForm(request.POST, instance=casa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Casa editada com sucesso!')
            return redirect('listar_casas')
        else:
            messages.error(request, 'Erro ao editar a casa. Verifique os dados e tente novamente.')
    else:
        form = CasaForm(instance=casa)
    return render(request, 'casas/editar_casa.html', {'form': form, 'casa': casa})
