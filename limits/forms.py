from django import forms
from .models import Limit


class LimitForm(forms.ModelForm):
    class Meta:
        model = Limit
        fields = ['contract']