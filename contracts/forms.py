from django import forms
from .models import PaymentDocument

class PaymentDocumentForm(forms.ModelForm):
    class Meta:
        model = PaymentDocument
        fields = ['contract', 'date_issued', 'document_name', 'amount', 'note']
        widgets = {
            'date_issued': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }
        labels = {
            'contract': 'Контракт',
            'date_issued': 'Дата документа',
            'document_name': 'Название документа',
            'amount': 'Сумма',
            'note': 'Примечание',
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Сумма должна быть положительной числом.")
        return amount
