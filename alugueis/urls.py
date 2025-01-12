from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alugueis, name='listar_alugueis'),
    path('cadastrar/', views.cadastrar_aluguel, name='cadastrar_aluguel'),
    path('registrar_pagamento/<int:pk>/', views.registrar_pagamento, name='registrar_pagamento'),
    path('registrar_pagamento_parcial/<int:pk>/', views.registrar_pagamento_parcial, name='registrar_pagamento_parcial'),
]
