from django import forms

from SGDR.models import SGDR

class SGDRForms(forms.ModelForm):
    class Meta:
        model = SGDR
        fields = ("__all__")