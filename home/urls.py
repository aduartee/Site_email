from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vod', views.vod, name='vod'),
    path('cdntv', views.cdntv, name='cdntv'),
    path('aplicativos',views.aplicativos, name='aplicativos'),
    ]