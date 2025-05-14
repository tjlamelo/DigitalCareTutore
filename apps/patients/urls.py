from django.urls import path
from .views import (
    register_patient,
    login_patient,
    patient_logout,
    patient_dashboard,
    complete_profile,
    add_emergency_contact
)
app_name = 'patients' 

urlpatterns = [
    path('register/', register_patient, name='patient_register'),
    path('login/', login_patient, name='patient_login'),
    path('logout/', patient_logout, name='patient_logout'),
    path('dashboard/', patient_dashboard, name='patient_dashboard'),
    path('complete-profile/', complete_profile, name='complete_profile'),
    path('add-contact/', add_emergency_contact, name='add_emergency_contact'),
]