from django.db import models
from patients.models import PatientProfile  

class RendezVous(models.Model):
    STATUT_CHOICES = [
        ('En attente', 'En attente'),
        ('Confirmé', 'Confirmé'),
        ('Annulé', 'Annulé'),
        ('Terminé', 'Terminé'),
    ]

    patient = models.ForeignKey(
        PatientProfile, 
        on_delete=models.CASCADE, 
        related_name='rendezvous_en_tant_que_patient'
    )
    medecin = models.ForeignKey(
        PatientProfile, 
        on_delete=models.CASCADE, 
        related_name='rendezvous_en_tant_que_medecin'
    )
    datePriseRendevous = models.DateTimeField()
    service = models.CharField(max_length=100)
    date_rdv = models.DateTimeField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='En attente')
    rappel_envoye = models.BooleanField(default=False)

    def __str__(self):
        return f"RDV entre {self.patient} et Dr. {self.medecin} le {self.date_rdv}"
