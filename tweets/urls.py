from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('buscar/semana/', views.busca_7_dias),
    path('buscar/mes/', views.busca_30_dias),
    path('busca-mensal/', views.busca_mensal),
    path('busca-semanal/', views.buscar),
    path('exemplos/', views.exemplos),
    path('sobre/', views.sobre),
]