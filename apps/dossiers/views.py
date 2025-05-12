# apps/dossiers/views.py

from django.shortcuts import render, redirect
from .models import DossierMedical

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

        # Conversions sécurisées
        def to_float(val):
            try:
                return float(val) if val else None
            except ValueError:
                return None

        def to_int(val):
            try:
                return int(val) if val else None
            except ValueError:
                return None

        # Création du dossier médical
        DossierMedical.objects.create(
            antecedents_medicaux=antecedents_medicaux,
            allergies=allergies,
            groupe_sanguin=groupe_sanguin,
            rhésus=rhésus,
            taille=to_float(taille),
            poids=to_float(poids),
            pression_arterielle=pression_arterielle,
            temperature_corporelle=to_float(temperature_corporelle),
            frequence_cardiaque=to_int(frequence_cardiaque),
            frequence_respiratoire=to_int(frequence_respiratoire),
            saturation_oxygene=to_int(saturation_oxygene),
            diagnostic=diagnostic,
            traitements_en_cours=traitements_en_cours,
            notes_medicales=notes_medicales,
            recommandations=recommandations
        )

        return redirect('liste_dossiers')  # Redirige vers une vue existante

    return render(request, 'dme/dossier.html')
def liste_dossiers_medicaux(request):
    dossiers = DossierMedical.objects.all()
    return render(request, 'dme.liste_dossiers.html', {'dossiers': dossiers})