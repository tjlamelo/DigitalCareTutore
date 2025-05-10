# apps/dossiers/views.py

from django.shortcuts import render, redirect
from .models import DossierMedical

def creer_dossier_medical(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire manuellement
        antecedents_medicaux = request.POST.get('antecedents_medicaux', '')
        allergies = request.POST.get('allergies', '')
        groupe_sanguin = request.POST.get('groupe_sanguin', '')
        rhésus = request.POST.get('rhésus', '')
        taille = request.POST.get('taille')
        poids = request.POST.get('poids')
        pression_artérielle = request.POST.get('pression_artérielle', '')

        # Conversion des nombres
        try:
            taille = float(taille) if taille else None
        except ValueError:
            taille = None

        try:
            poids = float(poids) if poids else None
        except ValueError:
            poids = None

        # Création du dossier médical
        DossierMedical.objects.create(
            antecedents_medicaux=antecedents_medicaux,
            allergies=allergies,
            groupe_sanguin=groupe_sanguin,
            rhésus=rhésus,
            taille=taille,
            poids=poids,
            pression_artérielle=pression_artérielle
        )

       # return redirect('liste_dossiers')  # Redirige vers la liste

    return render(request, 'dossier.html')


def liste_dossiers_medicaux(request):
    dossiers = DossierMedical.objects.all()
    return render(request, 'liste_dossiers.html', {'dossiers': dossiers})