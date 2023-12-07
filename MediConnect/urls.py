from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
    path('pw_change/', views.pw_change, name='pw_change'),
    path('register/', views.register, name='register'),
    path('employee_search/', views.employee_search, name='employee_search'),
    path('employee_update/', views.employee_update, name='employee_update'),
    path('hospital_registration/', views.hospital_registration, name='hospital_registration'),
    path('hospital_search/', views.hospital_search, name='hospital_search'),
    path('patient_registration/', views.patient_registration, name='patient_registration'),
    path('patient_all/', views.patient_all, name='patient_all'),
    path('patient_update/', views.patient_update, name='patient_update'),
    path('patient_expiration/', views.patient_expiration, name='patient_expiration'),
]
