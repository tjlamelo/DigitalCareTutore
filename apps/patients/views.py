from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rendezvous.models import RendezVous
from patients.models import PatientProfile

from .forms import (
    PatientRegistrationForm, 
    PatientLoginForm,
    PatientProfileForm,
    EmergencyContactForm
)
from .models import PatientProfile, EmergencyContact, UserRole
from patients.models import PatientProfile

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful! Please complete your profile.')
            return redirect('patients:patient_dashboard')  
    else:
        form = PatientRegistrationForm()
    return render(request, 'patients/register.html', {'form': form})

def login_patient(request):
    if request.method == 'POST':
        form = PatientLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return redirect('patients:patient_dashboard')  # ✅ Correction ici
    else:
        form = PatientLoginForm()
    return render(request, 'patients/login.html', {'form': form})

@login_required
def patient_logout(request):
    logout(request)
    return redirect('patients:patient_login')  

@login_required
def patient_dashboard(request):
    if not request.user.is_patient:
<<<<<<< HEAD
        return redirect('patients:patient_login') 
    
=======
        return redirect('patients:patient_login')

>>>>>>> rendez-vous
    try:
        profile = PatientProfile.objects.get(patient=request.user)
    except PatientProfile.DoesNotExist:
        profile = None

    emergency_contacts = EmergencyContact.objects.filter(patient=request.user)

    # ✅ ici on utilise bien le profil, pas le user
    mes_rendezvous = RendezVous.objects.filter(patient=profile)

    rendezvous_existe = mes_rendezvous.exists()

    context = {
        'profile': profile,
        'emergency_contacts': emergency_contacts,
        'rendezvous_existe': rendezvous_existe,
        'rendezvous': mes_rendezvous.first(),
        'mes_rendezvous': mes_rendezvous,
    }

    return render(request, 'patients/dashboard.html', context)



@login_required
def complete_profile(request):
    try:
        profile = request.user.profile
    except PatientProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.patient = request.user
            profile.save()
            request.user.profile_complete = True
            request.user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('patients:patient_dashboard')  
    else:
        form = PatientProfileForm(instance=profile)
    
    return render(request, 'patients/profile_form.html', {'form': form})

@login_required
def add_emergency_contact(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.patient = request.user
            contact.save()
            messages.success(request, 'Emergency contact added successfully!')
            return redirect('patients:patient_dashboard')  
    else:
        form = EmergencyContactForm()
    
    return render(request, 'patients/emergency_contacts.html', {'form': form})
@property
def is_medecin(self):
    return self.role == UserRole.MEDECIN

@property
def is_infirmier(self):
    return self.role == UserRole.PERSONNEL and hasattr(self, 'personnel') and self.personnel.poste == 'Infirmier'

@property
def is_personnel(self):
    return self.role == UserRole.PERSONNEL
