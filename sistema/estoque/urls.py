from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestao_estoque, name='gestao_estoque'),
]
