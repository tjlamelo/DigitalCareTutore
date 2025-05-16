from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    PatientRegistrationForm, 
    PatientLoginForm,
    PatientProfileForm,
    EmergencyContactForm
)
from .models import PatientProfile, EmergencyContact
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
                return redirect('patients:patient_dashboard')

    else:
        form = PatientLoginForm()
    return render(request, 'patients/login.html', {'form': form})

@login_required
def patient_logout(request):
    logout(request)
    return redirect('patient_login')

@login_required
def patient_dashboard(request):
    if not request.user.is_patient:
        return redirect('home')  # or appropriate page
    
    try:
        profile = request.user.profile
    except PatientProfile.DoesNotExist:
        profile = None
    
    context = {
        'profile': profile,
        'emergency_contacts': EmergencyContact.objects.filter(patient=request.user)
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
            return redirect('patient_dashboard')
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
            return redirect('patient_dashboard')
    else:
        form = EmergencyContactForm()
    
    return render(request, 'patients/emergency_contacts.html', {'form': form})