from django.contrib import admin  # Ajout de l'import manquant
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('personnel/', include('personnel.urls')),  # Si tu veux aussi ajouter les routes pour le personnel
    path('', views.base, name='base'),  # Redirige vers la vue home à la racine
]
