from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vod', views.vod, name='vod'),
    path('cdntv', views.cdntv, name='cdntv'),
    path('aplicativos',views.aplicativos, name='aplicativos'),
    path('down/', views.down, name='down'),
    path('downorigin/', views.downorigin, name='downorigin'),
    path('downedge/', views.downedge, name='downedge'),
	path('downvod/', views.downvod, name='downvod'),
    path('downoriginvod/', views.downoriginvod, name='downoriginvod'),
    path('downedgevod/', views.downedgevod, name='downedgevod'),
    path('downoriginedgevod', views.downoriginedgevod, name='downoriginedgevod')
    ]