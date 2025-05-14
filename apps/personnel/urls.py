from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_personnel, name='register_personnel'),
    path('login/', views.login_personnel, name='login_personnel'),
    path('logout/', views.personnel_logout, name='logout_personnel'),
    path('dashboard/', views.personnel_dashboard, name='personnel_dashboard'),
    path('profil/', views.complete_personnel_profile, name='complete_personnel_profile'),
]
