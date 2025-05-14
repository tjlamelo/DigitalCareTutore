# apps/dossiers/forms.py

from django import forms
from .models import (
    Allergie,
    AntecedentMedical,
    MesureClinique,
    Vaccination,
    Consultation,
    Hospitalisation
)

class AllergieForm(forms.ModelForm):
    class Meta:
        model = Allergie
        fields = ['nom', 'gravite']


class AntecedentMedicalForm(forms.ModelForm):
    class Meta:
        model = AntecedentMedical
        fields = ['type_antecedent', 'description', 'date']


class MesureCliniqueForm(forms.ModelForm):
    class Meta:
        model = MesureClinique
        fields = ['taille', 'poids', 'pression_arterielle']


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ['nom_vaccin', 'date_vaccination', 'dose']


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['motif_consultation', 'traitement_prescrit']


class HospitalisationForm(forms.ModelForm):
    class Meta:
        model = Hospitalisation
        fields = ['motif_hospitalisation', 'date_admission', 'date_sortie']