from django.urls import path
from . import views
app_name = 'rendezvous'
urlpatterns = [
    path('prise_rdv/', views.prise_rdv, name='prise_rdv'),
    path('modifier_rdv/<int:rdv_id>/', views.modifier_rdv, name='modifier_rdv'),
    path('supprimer/<int:rdv_id>/', views.supprimer_rdv, name='supprimer_rdv'),
]
