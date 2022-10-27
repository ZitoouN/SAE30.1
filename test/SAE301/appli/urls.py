from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil),
    path('home/', views.home),
    path('light1/', views.light1),
    path('light2/', views.light2),
    path('lights/', views.lights),
    path('temp/', views.temp),
    path('etat1/', views.etat1),
    path('etat2/', views.etat2),
]