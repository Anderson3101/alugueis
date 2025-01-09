from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_despesas, name='listar_despesas'),
    path('cadastrar/', views.cadastrar_despesa, name='cadastrar_despesa'),
    path('editar/<int:pk>/', views.editar_despesa, name='editar_despesa'),
    path('excluir/<int:pk>/', views.excluir_despesa, name='excluir_despesa'),
]
