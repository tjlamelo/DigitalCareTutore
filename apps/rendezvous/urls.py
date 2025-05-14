from django.urls import path
from . import views


urlpatterns = [
    path('rendezvous_create/', views.rendezvous_create, name='rendezvous_create'),
    path('file_attente_create/', views.file_attente_create, name='file_attente_create'),
]