from django import forms
from .models import Driver


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        exclude = []

