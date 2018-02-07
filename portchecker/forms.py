from django import forms
from .models import Ports

class PortCheckerForm(forms.Form):
    Port_to_check = forms.ModelChoiceField(queryset=Ports.objects.all())