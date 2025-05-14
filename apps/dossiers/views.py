from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import DossierMedical, Allergie, AntecedentMedical, MesureClinique, Vaccination, Consultation, Hospitalisation
from .forms import (
    AllergieForm, AntecedentMedicalForm, MesureCliniqueForm,
    VaccinationForm, ConsultationForm, HospitalisationForm
)

@login_required
def dossier_patient_view(request):
    dossier, _ = DossierMedical.objects.get_or_create(patient=request.user)

    model_form_map = {
        'allergie': (Allergie, AllergieForm),
        'antecedent': (AntecedentMedical, AntecedentMedicalForm),
        'mesure': (MesureClinique, MesureCliniqueForm),
        'vaccination': (Vaccination, VaccinationForm),
        'consultation': (Consultation, ConsultationForm),
        'hospitalisation': (Hospitalisation, HospitalisationForm),
    }

    modifier_type = request.GET.get('modifier')
    item_id = request.GET.get('id')
    type_form = request.GET.get('type_form') or request.POST.get('type_form')

    print("TYPE_FORM:", type_form)  # 👈 Affiche dans la console le type de formulaire demandé

    form = None

    if modifier_type and modifier_type in model_form_map and item_id:
        model_class, form_class = model_form_map[modifier_type]
        item = get_object_or_404(model_class, id=item_id, dossier=dossier)
        form = form_class(instance=item)
    elif type_form and type_form in model_form_map:
        model_class, form_class = model_form_map[type_form]
        form = form_class()
        print("FORMULAIRE CHARGÉ:", form_class.__name__)  # 👈 Pour voir quel formulaire est utilisé
    else:
        form = AllergieForm()

    # Gestion du POST
    if request.method == 'POST':
        type_form = request.POST.get('type_form')
        item_id = request.POST.get('item_id')

        if not type_form or type_form not in model_form_map:
            return redirect('dossiers:dashboard')

        model_class, form_class = model_form_map[type_form]

        if item_id:
            item = get_object_or_404(model_class, id=item_id, dossier=dossier)
            form = form_class(request.POST, instance=item)
        else:
            form = form_class(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.dossier = dossier
            obj.save()
            messages.success(request, f"{type_form.capitalize()} sauvegardé(e) avec succès.")
            return redirect('dossiers:dashboard')
        else:
            print("ERREURS DE FORMULAIRE:", form.errors)  # 👈 Affichage des erreurs

    context = {
        'dossier': dossier,
        'form': form,
        'modifier': bool(modifier_type and item_id),
        'modifier_type': modifier_type,
        'modifier_id': item_id,

        'allergies': dossier.allergies.all(),
        'antecedents': dossier.antecedents.all(),
        'mesures': dossier.mesures.all(),
        'vaccinations': dossier.vaccinations.all(),
        'consultations': dossier.consultations.all(),
        'hospitalisations': dossier.hospitalisations.all(),
    }

    return render(request, 'dme/dossier.html', context)
    dossier, _ = DossierMedical.objects.get_or_create(patient=request.user)

    model_form_map = {
        'allergie': (Allergie, AllergieForm),
        'antecedent': (AntecedentMedical, AntecedentMedicalForm),
        'mesure': (MesureClinique, MesureCliniqueForm),
        'vaccination': (Vaccination, VaccinationForm),
        'consultation': (Consultation, ConsultationForm),
        'hospitalisation': (Hospitalisation, HospitalisationForm),
    }

    # Récupère les paramètres GET/POST
    modifier_type = request.GET.get('modifier') or request.POST.get('modifier')
    item_id = request.GET.get('id') or request.POST.get('item_id')
    type_form = request.GET.get('type_form') or request.POST.get('type_form')

    form = None

    if modifier_type and modifier_type in model_form_map and item_id:
        model_class, form_class = model_form_map[modifier_type]
        item = get_object_or_404(model_class, id=item_id, dossier=dossier)
        form = form_class(instance=item)
    elif type_form and type_form in model_form_map:
        _, form_class = model_form_map[type_form]
        form = form_class()
    else:
        form = AllergieForm()

    # Gestion du POST
    if request.method == 'POST':
        type_form = request.POST.get('type_form')
        item_id = request.POST.get('item_id')

        if not type_form or type_form not in model_form_map:
            return redirect('dossiers:dashboard')

        model_class, form_class = model_form_map[type_form]

        if item_id:
            item = get_object_or_404(model_class, id=item_id, dossier=dossier)
            form = form_class(request.POST, instance=item)
        else:
            form = form_class(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.dossier = dossier
            obj.save()
            messages.success(request, f"{type_form.capitalize()} sauvegardé(e) avec succès.")
            return redirect('dossiers:dashboard')
        else:
            print("ERREURS DE FORMULAIRE:", form.errors)  # Debuggage utile pour toi

    context = {
        'dossier': dossier,
        'form': form,
        'modifier': bool(modifier_type and item_id),
        'modifier_type': modifier_type,
        'modifier_id': item_id,

        'allergies': dossier.allergies.all(),
        'antecedents': dossier.antecedents.all(),
        'mesures': dossier.mesures.all(),
        'vaccinations': dossier.vaccinations.all(),
        'consultations': dossier.consultations.all(),
        'hospitalisations': dossier.hospitalisations.all(),
    }

    return render(request, 'dme/dossier.html', context)