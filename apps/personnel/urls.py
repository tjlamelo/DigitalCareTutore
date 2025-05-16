from django.urls import path
from . import views
app_name = 'personnel'
urlpatterns = [
    path('register/', views.register_personnel, name='register_personnel'),
    path('login/', views.login_personnel, name='login_personnel'),
    path('logout/', views.personnel_logout, name='logout_personnel'),
    path('dashboard/', views.personnel_dashboard, name='personnel_dashboard'),
    path('profil/', views.complete_personnel_profile, name='complete_personnel_profile'),
    path('dashboard/medecin/', views.dashboard_medecin, name='dashboard_medecin'),
    path('dashboard/infirmier/', views.dashboard_infirmier, name='dashboard_infirmier'),
    path('dashboard/personnel/', views.dashboard_personnel, name='dashboard_personnel'),
]
