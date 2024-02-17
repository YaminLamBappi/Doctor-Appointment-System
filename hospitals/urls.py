from django.urls import path
from . import views


urlpatterns = [
    path('landing/', views.landing_page, name='landing_page'),
    path('add-hospital/', views.add_hospital, name='add_hospital'),  # URL pattern for form submission
]
