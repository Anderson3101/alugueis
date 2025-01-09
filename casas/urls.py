from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_casas, name='listar_casas'),
    path('cadastrar/', views.cadastrar_casa, name='cadastrar_casa'),
    path('editar/<int:pk>/', views.editar_casa, name='editar_casa'),  # Rota para editar casa
    path('excluir/<int:pk>/', views.excluir_casa, name='excluir_casa'),
]
