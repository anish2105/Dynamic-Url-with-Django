from django import forms
from .models import dict

class dictform(forms.ModelForm):
    class Meta:
        model = dict
        fields = ['letter','word','defi','example']
