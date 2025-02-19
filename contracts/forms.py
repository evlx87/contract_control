from django import forms
from django.core.exceptions import ValidationError

from .models import PaymentDocument, Contract, PaymentOrder, AdditionalAgreement


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

    def clean_contract_file(self):
        file = self.cleaned_data.get('contract_file')
        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError("Файл не подходящего формата. Загрузите скан документа в формате PDF.")
        return file


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

    def clean_payment_file(self):
        file = self.cleaned_data.get('payment_file')
        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError("Файл не подходящего формата. Загрузите скан документа в формате PDF.")
        return file

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

    def clean_pp_file(self):
        file = self.cleaned_data.get('pp_file')
        if file:
            if not file.name.endswith('.pdf'):
                raise ValidationError("Файл не подходящего формата. Загрузите скан документа в формате PDF.")
        return file


class AdditionalAgreementForm(forms.ModelForm):
    class Meta:
        model = AdditionalAgreement
        fields = ['date', 'number', 'agreement_file']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }