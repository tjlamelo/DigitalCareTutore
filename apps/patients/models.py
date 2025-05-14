from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Rôles dans le système
class UserRole(models.TextChoices):
    PATIENT = 'PATIENT', 'Patient'
    MEDECIN = 'MEDECIN', 'Médecin'
    PERSONNEL = 'PERSONNEL', 'Personnel de santé'

# Modèle utilisateur personnalisé
class Patient(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.PATIENT
    )
    profile_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def is_medecin(self):
        return self.role == UserRole.MEDECIN

    def is_personnel_sante(self):
        return self.role == UserRole.PERSONNEL

    def is_patient(self):
        return self.role == UserRole.PATIENT

# Profil lié à l'utilisateur
class PatientProfile(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('M', 'Male'), ('F', 'Female')],
        blank=True
    )
    address = models.TextField(blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Format: '+999999999'"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return f"Profil de {self.patient.username}"

# Contact d'urgence
class EmergencyContact(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='emergency_contacts')
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Format: '+999999999'"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.relationship})"
