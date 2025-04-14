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

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if KBK.objects.filter(code=code).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Код КБК уже существует.')
        return code

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

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if KOSGU.objects.filter(code=code).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Код КОСГУ уже существует.')
        return code
