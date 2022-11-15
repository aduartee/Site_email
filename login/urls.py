from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/',views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('valida_cadastro', views.valida_cadastro, name='valida_cadastro'),  
    ]