from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/casa/', views.cadastrar_casa, name='cadastrar_casa'),
    path('listar/casas/', views.listar_casas, name='listar_casas'),
    path('cadastrar/aluguel/', views.cadastrar_aluguel, name='cadastrar_aluguel'),
    path('listar/alugueis/', views.listar_alugueis, name='listar_alugueis'),
    path('detalhes/financeiros/', views.detalhes_financeiros, name='detalhes_financeiros'),
]
