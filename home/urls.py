from django.urls import path
from . import views

urlpatterns = [
    path('entrar', views.entrar_home, name='entrar_home'),
    path('criar_email', views.criar_email, name='criar_email'),
]