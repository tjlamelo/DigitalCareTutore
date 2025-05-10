from django.urls import path
from . import views

app_name = 'dossiers'

urlpatterns = [
    path('nouveau/', views.creer_dossier_medical, name='creer_dossier'),
    path('liste/', views.liste_dossiers_medicaux, name='liste_dossiers'),
]