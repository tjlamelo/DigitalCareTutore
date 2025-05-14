from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, PersonnelProfile

class PersonnelRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')

class PersonnelLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class PersonnelProfileForm(forms.ModelForm):
    class Meta:
        model = PersonnelProfile
        exclude = ('user',)
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_recrutement': forms.DateInput(attrs={'type': 'date'}),
        }