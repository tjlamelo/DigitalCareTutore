from django.urls import path
from . import views

app_name = 'dossiers'

urlpatterns = [
    path('mon-dossier/', views.dossier_patient_view, name='dashboard'),
    path('mon-dossier/allergie/ajouter/<int:dossier_id>/', views.ajouter_allergie, name='ajouter_allergie'),
    path('mon-dossier/antecedent/ajouter/<int:dossier_id>/', views.ajouter_antecedent, name='ajouter_antecedent'),
    path('mon-dossier/mesure/ajouter/<int:dossier_id>/', views.ajouter_mesure, name='ajouter_mesure'),
    path('mon-dossier/vaccination/ajouter/<int:dossier_id>/', views.ajouter_vaccination, name='ajouter_vaccination'),
    path('mon-dossier/consultation/ajouter/<int:dossier_id>/', views.ajouter_consultation, name='ajouter_consultation'),
    path('mon-dossier/hospitalisation/ajouter/<int:dossier_id>/', views.ajouter_hospitalisation, name='ajouter_hospitalisation'),
]