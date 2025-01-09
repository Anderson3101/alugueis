from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alugueis, name='listar_alugueis'),
    path('cadastrar/', views.cadastrar_aluguel, name='cadastrar_aluguel'),
]
