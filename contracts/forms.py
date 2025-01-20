from django import forms

from .models import PaymentDocument, Contract, PaymentOrder


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = (
            'kbk_type',
            'kosgu_type',
            'name',
            'purchase_type',
            'contract_type',
            'supplier',
            'contract_subject',
            'contract_number',
            'contract_date',
            'contract_duration',
            'service_start_date',
            'service_end_date',
            'contract_amount',
            'contract_file',
            'contract_year')

        widgets = {
            'contract_date': forms.DateInput(format='d.m.y', attrs={'type': 'date'}),
            'contract_duration': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'service_start_date': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'service_end_date': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            'contract_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100})}


class PaymentDocumentForm(forms.ModelForm):
    class Meta:
        model = PaymentDocument
        fields = [
            'contract',
            'date_issued',
            'document_name',
            'amount',
            'payment_file']
        widgets = {
            'date_issued': forms.DateInput(
                format='%d.%m.%Y', attrs={
                    'type': 'date'}), 'document_name': forms.Textarea(
                attrs={
                    'rows': 4, 'cols': 40})}
        labels = {
            'contract': 'Контракт',
            'date_issued': 'Дата документа',
            'document_name': 'Наименование и номер документа',
            'amount': 'Сумма',
        }
        exclude = ['contract']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError(
                "Сумма должна быть положительной числом.")
        return amount


class PaymentOrderForm(forms.ModelForm):
    class Meta:
        model = PaymentOrder
        fields = ['contract', 'pp_date', 'pp_name', 'pp_amount', 'pp_file']
        widgets = {
            'pp_date': forms.DateInput(
                format='%d.%m.%Y', attrs={
                    'type': 'date'}), 'pp_name': forms.Textarea(
                attrs={
                    'rows': 3, 'cols': 40}), }
        labels = {
            'contract': 'Контракт',
            'pp_date': 'Дата платежного поручения',
            'pp_name': 'Наименование платежного поручения',
            'pp_amount': 'Оплаченная сумма',
        }
        exclude = ['contract']
