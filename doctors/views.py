from django.shortcuts import render
from .models import Doctor

def doctor_profile(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request, 'profile.html', {'doctor': doctor})


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})
