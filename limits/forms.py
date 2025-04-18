from django import forms
from django.utils.translation import gettext_lazy as _

from lib_ccportal.models import KBK, KOSGU, PurchaseObject
from limits.models import Limit


class LimitForm(forms.ModelForm):
    name = forms.ChoiceField(  # Используем ChoiceField для наименования объекта закупки
        choices=[],  # Сначала оставляем пустым
        label=_("Наименование объекта закупки")
    )

    kbk = forms.ModelChoiceField(
        queryset=KBK.objects.all(),
        label=_("КБК")
    )

    kosgu = forms.ModelChoiceField(
        queryset=KOSGU.objects.all(),
        label=_("КОСГУ")
    )

    amount = forms.DecimalField(label=_("Сумма доведенных лимитов"))

    class Meta:
        model = Limit  # Указываем модель, с которой работает форма
        fields = ['name', 'kbk', 'kosgu', 'amount']  # Указываем поля, которые будут включены в форму

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Заполняем choices для поля name на основе данных из модели PurchaseObject
        self.fields['name'].choices = [(purchase.code, purchase.description) for purchase in
                                       PurchaseObject.objects.all()]
    def clean(self):
        cleaned_data = super().clean()
        kbk_code = cleaned_data.get("kbk")
        kosgu_code = cleaned_data.get("kosgu")

        if kbk_code:
            try:
                cleaned_data['kbk'] = KBK.objects.get(code=kbk_code)
            except KBK.DoesNotExist:
                self.add_error('kbk', _("Выбранный КБК не существует."))

        if kosgu_code:
            try:
                cleaned_data['kosgu'] = KOSGU.objects.get(code=kosgu_code)
            except KOSGU.DoesNotExist:
                self.add_error('kosgu', _("Выбранный КОСГУ не существует."))

        return cleaned_data

