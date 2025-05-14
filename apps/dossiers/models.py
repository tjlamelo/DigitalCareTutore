from django.db import models
from enum import Enum

# --- Modèle Patient ---
# Tu peux décommenter cette ligne si tu as déjà un modèle Patient existant
 
from patients.models import Patient   

class DossierMedical(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dossier médical de {self.patient.username}"
 

    class Meta:
        verbose_name = "Dossier médical"
        verbose_name_plural = "Dossiers médicaux"


# --- Enumérations pour les champs prédéfinis ---

class GroupeSanguin(Enum):
    A = 'A'
    B = 'B'
    AB = 'AB'
    O = 'O'

class Rhésus(Enum):
    POSITIF = '+'
    NEGATIF = '-'

class GraviteAllergie(Enum):
    LEGER = 'Légère'
    MODERE = 'Modérée'
    GRAVE = 'Grave'
    ANAPHYLACTIQUE = 'Anaphylactique'

class TypeAntecedent(Enum):
    CHRONIQUE = 'Chronique'
    AIGU = 'Aigu'
    FAMILIAL = 'Familial'
    HEREDITAIRE = 'Héréditaire'

class PressionArterielle(Enum):
    NORMALE = 'Normale'
    HYPERTENSION_LEGERE = 'Hypertension légère'
    HYPERTENSION_SEVERE = 'Hypertension sévère'


# --- Modèle Allergie ---
class Allergie(models.Model):
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE, related_name='allergies')
    nom = models.CharField(max_length=100)
    gravite = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in GraviteAllergie],
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nom} (Gravité: {self.gravite})"


# --- Modèle Antécédent Médical ---
class AntecedentMedical(models.Model):
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE, related_name='antecedents')
    description = models.TextField()
    type_antecedent = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in TypeAntecedent],
        blank=True,
        null=True
    )
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Antécédent médical: {self.type_antecedent} - {self.description}"


# --- Modèle Mesure Clinique ---
class MesureClinique(models.Model):
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE, related_name='mesures')
    taille = models.FloatField(null=True, blank=True)
    poids = models.FloatField(null=True, blank=True)
    pression_arterielle = models.CharField(
        max_length=30,
        choices=[(tag.name, tag.value) for tag in PressionArterielle],
        null=True,
        blank=True
    )
    date_mesure = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesure clinique du {self.date_mesure.strftime('%Y-%m-%d %H:%M:%S')}"


# --- Modèle Vaccination ---
class Vaccination(models.Model):
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE, related_name='vaccinations')
    nom_vaccin = models.CharField(max_length=100)
    date_vaccination = models.DateField()
    dose = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nom_vaccin} (Date: {self.date_vaccination})"


# --- Modèle Consultation ---
class Consultation(models.Model):
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE, related_name='consultations')
    date_consultation = models.DateTimeField(auto_now_add=True)
    motif_consultation = models.CharField(max_length=255)
    traitement_prescrit = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consultation du {self.date_consultation.strftime('%Y-%m-%d %H:%M:%S')} - Motif: {self.motif_consultation}"


# --- Modèle Hospitalisation ---
class Hospitalisation(models.Model):
    dossier = models.ForeignKey(DossierMedical, on_delete=models.CASCADE, related_name='hospitalisations')
    date_admission = models.DateTimeField()
    date_sortie = models.DateTimeField(null=True, blank=True)
    motif_hospitalisation = models.CharField(max_length=255)

    def __str__(self):
        return f"Hospitalisation du {self.date_admission.strftime('%Y-%m-%d %H:%M:%S')} - Motif: {self.motif_hospitalisation}"

