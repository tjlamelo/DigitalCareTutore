from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    PersonnelRegistrationForm, 
    PersonnelLoginForm,
    PersonnelProfileForm,
)
from .models import PersonnelProfile

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
        profile = request.user.profile
    except PersonnelProfile.DoesNotExist:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, 'personnel/dashboard.html', context)

@login_required
def complete_personnel_profile(request):
    try:
        profile = request.user.profile
    except PersonnelProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = PersonnelProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            request.user.profile_complete = True
            request.user.save()
            messages.success(request, 'Profil mis à jour avec succès.')
            return redirect('personnel_dashboard')
    else:
        form = PersonnelProfileForm(instance=profile)

    return render(request, 'personnel/profile_form.html', {'form': form})