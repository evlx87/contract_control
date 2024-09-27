from django import forms

from .choice_objects import PURCHASE_ODJ_CHOICE, KBK_TYPE_CHOICES, KOSGU_TYPE_CHOICES
from .models import Limit


class LimitForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=[
            (key,
             value) for key,
            value in PURCHASE_ODJ_CHOICE.items()],
        label='Наименование объекта закупки')
    kbk_type = forms.ChoiceField(choices=KBK_TYPE_CHOICES, label='КБК')
    kosgu_type = forms.ChoiceField(choices=KOSGU_TYPE_CHOICES, label='КОСГУ')
    amount = forms.DecimalField(label='Сумма доведенных лимитов')

    class Meta:
        model = Limit
        fields = ['name', 'kbk_type', 'kosgu_type', 'amount']
