from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from patients.models import Patient, PatientProfile  # ✅ modèles corrects

# Formulaire d'inscription du personnel
class PersonnelRegistrationForm(UserCreationForm):
    class Meta:
        model = Patient  # ✅ Utilise désormais Patient au lieu de CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')

# Formulaire de connexion du personnel
class PersonnelLoginForm(AuthenticationForm):
    class Meta:
        model = Patient  # ✅ même correction ici
        fields = ('username', 'password')

# Formulaire de profil du personnel
class PersonnelProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile  # ✅ modèle de profil lié
        exclude = ('patient',)  # ✅ champ OneToOneField mis à jour
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
