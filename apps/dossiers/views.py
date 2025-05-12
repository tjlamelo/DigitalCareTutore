from django.shortcuts import render, redirect
from .models import (
    DossierMedical, Allergie, AntecedentMedical, MesureClinique,
    GraviteAllergie, TypeAntecedent, PressionArterielle, GroupeSanguin, Rhésus
)

def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

def creer_dossier_medical(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        antecedents_medicaux = request.POST.get('antecedents_medicaux', '')
        allergies = request.POST.get('allergies', '')
        groupe_sanguin = request.POST.get('groupe_sanguin', '')
        rhésus = request.POST.get('rhésus', '')
        taille = request.POST.get('taille')
        poids = request.POST.get('poids')
        pression_arterielle = request.POST.get('pression_arterielle', '')
        temperature_corporelle = request.POST.get('temperature_corporelle')
        frequence_cardiaque = request.POST.get('frequence_cardiaque')
        frequence_respiratoire = request.POST.get('frequence_respiratoire')
        saturation_oxygene = request.POST.get('saturation_oxygene')
        diagnostic = request.POST.get('diagnostic', '')
        traitements_en_cours = request.POST.get('traitements_en_cours', '')
        notes_medicales = request.POST.get('notes_medicales', '')
        recommandations = request.POST.get('recommandations', '')

        # Création du dossier médical
        dossier = DossierMedical.objects.create()

        # Ajouter les allergies
        if allergies:
            allergies_list = allergies.split(',')
            for allergie in allergies_list:
                Allergie.objects.create(dossier=dossier, nom=allergie.strip())

        # Ajouter les antécédents médicaux
        if antecedents_medicaux:
            antecedents_list = antecedents_medicaux.split(',')
            for antecedent in antecedents_list:
                AntecedentMedical.objects.create(dossier=dossier, description=antecedent.strip())

        # Ajouter les mesures cliniques
        if any([taille, poids, pression_arterielle, temperature_corporelle, frequence_cardiaque, frequence_respiratoire, saturation_oxygene]):
            MesureClinique.objects.create(
                dossier=dossier,
                taille=to_float(taille),
                poids=to_float(poids),
                pression_arterielle=pression_arterielle or None,
                # Tu peux ajouter ici les autres champs si définis dans ton modèle
            )

        # TODO : Ajoute ici la logique pour diagnostic, traitements, etc. si les modèles les prévoient

        return redirect('liste_dossiers')

    # --- GET request : charger les enums dynamiquement ---
    context = {
        'gravite_allergies': [(e.name, e.value) for e in GraviteAllergie],
        'types_antecedents': [(e.name, e.value) for e in TypeAntecedent],
        'pressions_arterielles': [(e.name, e.value) for e in PressionArterielle],
        'groupes_sanguins': [(e.name, e.value) for e in GroupeSanguin],
        'rhesus_options': [(e.name, e.value) for e in Rhésus],
    }
    return render(request, 'dme/dossier.html', context)
