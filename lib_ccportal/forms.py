from django import forms
from .models import KBK, KOSGU

class KBKForm(forms.ModelForm):
    class Meta:
        model = KBK
        fields = ['code', 'description']
        labels = {
            'code': 'Код КБК',
            'description': 'Описание',
        }
        widgets = {
            'code': forms.TextInput(attrs={'required': True}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class KOSGUForm(forms.ModelForm):
    class Meta:
        model = KOSGU
        fields = ['code', 'description']
        labels = {
            'code': 'Код КОСГУ',
            'description': 'Описание',
        }
        widgets = {
            'code': forms.TextInput(attrs={'required': True}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }