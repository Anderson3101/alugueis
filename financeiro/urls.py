from django.urls import path
from . import views

urlpatterns = [
    path('detalhes/', views.detalhes_financeiros, name='detalhes_financeiros'),
    path('registrar_pagamento/<int:pk>/', views.registrar_pagamento, name='registrar_pagamento'),
]
