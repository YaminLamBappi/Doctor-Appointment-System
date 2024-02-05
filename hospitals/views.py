# hospitals/views.py
from django.shortcuts import render, redirect
from .forms import HospitalForm

def landing_page(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')  # Redirect to the landing page after form submission
    else:
        form = HospitalForm()
    return render(request, 'landing_page.html', {'title': 'Hospital Management System', 'form': form})


def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')  # Redirect to the landing page after form submission
    else:
        form = HospitalForm()
    return render(request, 'add_hospital.html', {'form': form})
