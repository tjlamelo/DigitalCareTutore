
# Create your views here.
from django.urls import path
from . import views
from datetime import datetime
from patients.models import PatientProfile
from django.http import HttpResponse
from rendezvous.models import RendezVous
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect


def prise_rdv(request):
    if request.method == "POST":
        try:
            # On suppose que le patient est déjà authentifié
            # et que son profil est accessible via request.user
            patient_profile = PatientProfile.objects.get(patient=request.user)
        except PatientProfile.DoesNotExist:
            return HttpResponse("Profil patient introuvable.", status=400)

        try:
            medecin_profile = PatientProfile.objects.get(id=request.POST["medecin"])
            if medecin_profile.patient.role != 'MEDECIN':
                return HttpResponse("Médecin invalide.", status=400)
        except PatientProfile.DoesNotExist:
            return HttpResponse("Médecin invalide.", status=400)

        try:
            datePriseRendevous = datetime.strptime(request.POST["datePriseRendevous"], "%Y-%m-%dT%H:%M")
            date_rdv = datetime.strptime(request.POST["date_rdv"], "%Y-%m-%dT%H:%M")
        except (ValueError, KeyError):
            return HttpResponse("Format de date invalide.", status=400)

        RendezVous.objects.create(
            patient=patient_profile,
            medecin=medecin_profile,
            datePriseRendevous=datePriseRendevous,
            date_rdv=date_rdv,
            service=request.POST["service"],
            statut=request.POST.get("statut", "En attente"),
            rappel_envoye="rappel_envoye" in request.POST
        )


    # GET
    medecins = PatientProfile.objects.filter(patient__role='MEDECIN')
    profile = getattr(request.user, 'profile', None)

    return render(request, "rendez-vous/rendez-vous.html", {
        "medecins": medecins,
        "profile": profile,
    })


def modifier_rdv(request, rdv_id):
    rdv = get_object_or_404(RendezVous, id=rdv_id)
    if request.method == "POST":
        rdv.patient_id = request.POST["patient"]
        rdv.medecin_id = request.POST["medecin"]
        rdv.datePriseRendevous = request.POST["datePriseRendevous"]
        rdv.date_rdv = request.POST["date_rdv"]
        rdv.service = request.POST["service"]
        rdv.statut = request.POST["statut"]
        rdv.rappel_envoye = "rappel_envoye" in request.POST
        rdv.save()

    patients_profiles = PatientProfile.objects.filter(patient__role="PATIENT")
    medecins = PatientProfile.objects.filter(patient__role="MEDECIN")
    statuts = ["En attente", "Confirmé", "Annulé", "Terminé"]

    return render(request, "rendez-vous/rendez.html", {
        "rdv": rdv,
        "patients": patients_profiles,
        "medecins": medecins,
        "statuts": statuts,
        "is_edit": True,
    })

def supprimer_rdv(request, rdv_id):
    rendezvous = get_object_or_404(RendezVous, id=rdv_id)

    # Optionnel : Vérifie que l'utilisateur a le droit de supprimer ce RDV
    if request.user != rendezvous.patient.patient:
        return redirect('patients:patient_dashboard')  # ou une page d'erreur

    rendezvous.delete()
    return redirect('patients:patient_dashboard')
