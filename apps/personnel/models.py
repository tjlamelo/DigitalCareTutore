from django.db import models
from patients.models import Patient  # Le modèle utilisateur personnalisé
from django.core.validators import RegexValidator

# Spécialités médicales (tu peux les adapter selon tes besoins)
class Specialite(models.TextChoices):
    GENERALISTE = 'GENERALISTE', 'Médecin généraliste'
    PEDIATRIE = 'PEDIATRIE', 'Pédiatrie'
    CARDIOLOGIE = 'CARDIOLOGIE', 'Cardiologie'
    GYNECOLOGIE = 'GYNECOLOGIE', 'Gynécologie'
    INFIRMIER = 'INFIRMIER', 'Infirmier'
    AUTRE = 'AUTRE', 'Autre'

# Services hospitaliers
class Service(models.TextChoices):
    URGENCE = 'URGENCE', 'Urgences'
    CONSULTATION = 'CONSULTATION', 'Consultation externe'
    HOSPITALISATION = 'HOSPITALISATION', 'Hospitalisation'
    CHIRURGIE = 'CHIRURGIE', 'Chirurgie'
    LABORATOIRE = 'LABORATOIRE', 'Laboratoire'
    AUTRE = 'AUTRE', 'Autre'

class PersonnelSante(models.Model):
    utilisateur = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='personnel')
    specialite = models.CharField(max_length=50, choices=Specialite.choices)
    service = models.CharField(max_length=50, choices=Service.choices)
    matricule = models.CharField(max_length=30, unique=True)
    poste = models.CharField(max_length=100, blank=True)
    date_recrutement = models.DateField(null=True, blank=True)
    is_actif = models.BooleanField(default=True)

 

    class Meta:
        verbose_name = "Personnel de santé"
        verbose_name_plural = "Personnel de santé"

    def __str__(self):
        return f"{self.utilisateur.get_full_name()} - {self.specialite}"

    def est_medecin(self):
        return self.specialite in [
            Specialite.GENERALISTE,
            Specialite.CARDIOLOGIE,
            Specialite.PEDIATRIE,
            Specialite.GYNECOLOGIE,
        ]

    def est_infirmier(self):
        return self.specialite == Specialite.INFIRMIER
