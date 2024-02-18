from django.urls import path
from .views import doctor_profile, doctor_list

urlpatterns = [
    path('<int:doctor_id>/', doctor_profile, name='doctor_profile'),
    path('doctors/', doctor_list, name='doctor_list'),
]