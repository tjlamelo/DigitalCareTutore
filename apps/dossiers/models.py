 
from django.db import models
# from patients.models import Patient  

class DossierMedical(models.Model):
    # patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='dossier_medical')
    antecedents_medicaux = models.TextField(blank=True, null=True, verbose_name="Antécédents médicaux")
    allergies = models.TextField(blank=True, null=True, verbose_name="Allergies")
    groupe_sanguin = models.CharField(max_length=5, blank=True, null=True, verbose_name="Groupe sanguin")
    rhésus = models.CharField(max_length=1, choices=[('+', '+'), ('-', '-')], blank=True, null=True)
    taille = models.FloatField(blank=True, null=True, verbose_name="Taille (cm)")
    poids = models.FloatField(blank=True, null=True, verbose_name="Poids (kg)")
    pression_artérielle = models.CharField(max_length=7, blank=True, null=True, verbose_name="Pression artérielle (ex: 12/8)")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return f"Dossier médical de {self.patient}"

    class Meta:
        verbose_name = "Dossier médical"
        verbose_name_plural = "Dossiers médicaux"