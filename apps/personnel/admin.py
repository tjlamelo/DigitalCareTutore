from django.contrib import admin
from .models import PersonnelSante

@admin.register(PersonnelSante)
class PersonnelSanteAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'specialite', 'service', 'matricule', 'is_actif')
    search_fields = ('utilisateur__username', 'matricule', 'specialite')
