from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

from .forms import (
    PersonnelRegistrationForm, 
    PersonnelLoginForm,
    PersonnelProfileForm,
)

from patients.models import Patient, PatientProfile, UserRole  # 🔄 Correction ici

def home(request):
    return render(request, 'base.html')


def register_personnel(request):
    if request.method == 'POST':
        form = PersonnelRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Inscription réussie. Veuillez compléter votre profil.')
            return redirect('personnel_dashboard')
    else:
        form = PersonnelRegistrationForm()
    return render(request, 'personnel/register.html', {'form': form})


def login_personnel(request):
    if request.method == 'POST':
        form = PersonnelLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('personnel_dashboard')
    else:
        form = PersonnelLoginForm()
    return render(request, 'personnel/login.html', {'form': form})


@login_required
def personnel_logout(request):
    logout(request)
    return redirect('login_personnel')


@login_required
def personnel_dashboard(request):
    try:
        profile = request.user.profile  # fonctionne avec related_name='profile'
    except PatientProfile.DoesNotExist:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, 'personnel/dashboard.html', context)


@login_required
def complete_personnel_profile(request):
    try:
        profile = request.user.profile
    except PatientProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = PersonnelProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.patient = request.user  # ⚠️ champ = 'patient', pas 'user'
            profile.save()
            request.user.profile_complete = True
            request.user.save()
            messages.success(request, 'Profil mis à jour avec succès.')
            return redirect('personnel_dashboard')
    else:
        form = PersonnelProfileForm(instance=profile)

    return render(request, 'personnel/profile_form.html', {'form': form})

@login_required
def dashboard_medecin(request):
    if not request.user.is_medecin:
        return HttpResponseForbidden("Accès refusé.")

    # Récupère tous les patients
    patients = Patient.objects.filter(role=UserRole.PATIENT)
    patient_id = request.GET.get('patient')
    if patient_id:
        patient = get_object_or_404(Patient, id=patient_id)
    else:
        patient = patients.first()  # Sélection automatique du premier patient

    # Récupère le profil du patient sélectionné
    try:
        profile = patient.profile
    except (AttributeError, PatientProfile.DoesNotExist):
        profile = None

    context = {
        'patients': patients,
        'patient': patient,
        'profile': profile,
    }
    return render(request, 'personnel/dashboard_medecin.html', context)

@login_required
def dashboard_infirmier(request):
    if not request.user.is_infirmier:
        return HttpResponseForbidden("Accès refusé.")
    return render(request, 'personnel/dashboard_infirmier.html')

@login_required
def dashboard_personnel(request):
    if not request.user.is_personnel:
        return HttpResponseForbidden("Accès refusé.")
    return render(request, 'personnel/dashboard_personnel.html')