# filepath: c:\Users\USER\DigitalCareTutore\digitalcare\views.py
from django.http import HttpResponse

def base(request):
    return HttpResponse("Bienvenue sur la page d'accueil.")