from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Patient, PatientProfile, EmergencyContact

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = ('username', 'email', 'password1', 'password2')

class PatientLoginForm(AuthenticationForm):
    class Meta:
        model = Patient
        fields = ('username', 'password')

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        exclude = ('patient',)
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        exclude = ('patient',)