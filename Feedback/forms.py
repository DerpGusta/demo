from django import forms
from .import models


class PatientUpdationForm(forms.Form):
    Rating=forms.CharField()
    department=forms.CharField()
    area_of_issue=forms.CharField()
    explanation=forms.CharField()

class PatientCreationForm(forms.Form):
    patient_ID=forms.CharField()


class HODCreationForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()

class UserLoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()
    


    
