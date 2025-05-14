# apps/dossiers/urls.py

from django.urls import path
from . import views

app_name = 'dossiers'

urlpatterns = [
    # Vue principale du dossier (création + modification + affichage)
    path('mon-dossier/', views.dossier_patient_view, name='dashboard'),
]