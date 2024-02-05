# hospitals/forms.py
from django import forms
from .models import Hospital

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone_number', 'email', 'website', 'capacity']
