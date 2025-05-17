from django.shortcuts import render, redirect, get_object_or_404
from .models import DossierMedical, Allergie, AntecedentMedical, MesureClinique, Vaccination, Consultation, Hospitalisation, GraviteAllergie, TypeAntecedent, PressionArterielle
from .forms import AllergieForm, AntecedentMedicalForm, MesureCliniqueForm, VaccinationForm, ConsultationForm, HospitalisationForm

def dossier_patient_view(request):
    dossier = get_object_or_404(DossierMedical, patient=request.user)
    return render(request, 'dme/dashboard.html', {'dossier': dossier})

def ajouter_allergie(request, dossier_id):
    dossier = get_object_or_404(DossierMedical, id=dossier_id)

    if request.method == 'POST':
        form = AllergieForm(request.POST)
        if form.is_valid():
            allergie = form.save(commit=False)
            allergie.dossier = dossier
            allergie.save()
            return redirect('dossiers:dashboard')
    else:
        form = AllergieForm()

    gravite_allergies = [(tag.name, tag.value) for tag in GraviteAllergie]
    return render(request, 'dme/allergie_form.html', {
        'form': form,
        'gravite_allergies': gravite_allergies,
        'dossier_id': dossier_id
    })

def ajouter_antecedent(request, dossier_id):
    dossier = get_object_or_404(DossierMedical, id=dossier_id)

    # Récupérer les antécédents liés au dossier
    antecedents = AntecedentMedical.objects.filter(dossier=dossier)

    if request.method == 'POST':
        form = AntecedentMedicalForm(request.POST)
        if form.is_valid():
            antecedent = form.save(commit=False)
            antecedent.dossier = dossier
            antecedent.save()
            return redirect('dossiers:dashboard')
    else:
        form = AntecedentMedicalForm()

    type_antecedents = [(tag.name, tag.value) for tag in TypeAntecedent]
    return render(request, 'dme/antecedent_form.html', {
        'form': form,
        'type_antecedents': type_antecedents,
        'dossier_id': dossier_id,
        'antecedents': antecedents  
    })

def ajouter_mesure(request, dossier_id):
    dossier = get_object_or_404(DossierMedical, id=dossier_id)

    if request.method == 'POST':
        form = MesureCliniqueForm(request.POST)
        if form.is_valid():
            mesure = form.save(commit=False)
            mesure.dossier = dossier
            mesure.save()
            return redirect('dossiers:dashboard')
    else:
        form = MesureCliniqueForm()

    pression_choices = [(tag.name, tag.value) for tag in PressionArterielle]
    return render(request, 'dme/mesure_form.html', {
        'form': form,
        'pression_choices': pression_choices,
        'dossier_id': dossier_id
    })

def ajouter_vaccination(request, dossier_id):
    dossier = get_object_or_404(DossierMedical, id=dossier_id)

    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            vaccination = form.save(commit=False)
            vaccination.dossier = dossier
            vaccination.save()
            return redirect('dossiers:dashboard')
    else:
        form = VaccinationForm()

    return render(request, 'dme/vaccination_form.html', {'form': form, 'dossier_id': dossier_id})

def ajouter_consultation(request, dossier_id):
    dossier = get_object_or_404(DossierMedical, id=dossier_id)

    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.dossier = dossier
            consultation.save()
            return redirect('dossiers:dashboard')
    else:
        form = ConsultationForm()

    return render(request, 'dme/consultation_form.html', {'form': form, 'dossier_id': dossier_id})

def ajouter_hospitalisation(request, dossier_id):
    dossier = get_object_or_404(DossierMedical, id=dossier_id)

    if request.method == 'POST':
        form = HospitalisationForm(request.POST)
        if form.is_valid():
            hospitalisation = form.save(commit=False)
            hospitalisation.dossier = dossier
            hospitalisation.save()
            return redirect('dossiers:dashboard')
    else:
        form = HospitalisationForm()

    return render(request, 'dme/hospitalisation_form.html', {'form': form, 'dossier_id': dossier_id})