from django import forms
from .models import PaymentDocument, Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('name',
                  'purchase_type',
                  'funds_allocated',
                  'supplier',
                  'contract_subject',
                  'contract_number',
                  'contract_date',
                  'contract_duration',
                  'service_start_date',
                  'service_end_date',
                  'contract_amount')

        widgets = {
            'contract_date': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'contract_duration': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'service_start_date': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'service_end_date': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
        }


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
