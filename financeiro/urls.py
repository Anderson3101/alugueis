from django.urls import path
from . import views

urlpatterns = [
    path('', views.detalhes_financeiros, name='detalhes_financeiros'),
]
