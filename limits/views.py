from datetime import datetime
from decimal import Decimal

from django.contrib import messages
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from contracts.models import Contract
from lib_ccportal.models import PurchaseObject, KBK, KOSGU
from .forms import LimitForm
from .models import Limit


class LimitListView(ListView):
    model = Limit
    template_name = 'limits/limits_list.html'
    context_object_name = 'limits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        summary = []

        for limit in context['limits']:
            # Фильтрация контрактов по КБК, КОСГУ и году
            contracts = Contract.objects.filter(
                kbk_type=limit.kbk,
                kosgu_type=limit.kosgu,
                contract_date__year=limit.year
            )

            # Сумма цен контрактов
            total_contract_amount = contracts.aggregate(total=models.Sum('contract_amount'))['total'] or Decimal('0.00')

            # Остаток по лимиту
            remaining_amount = Decimal(limit.amount) - total_contract_amount

            summary.append({
                'kbk': limit.kbk,
                'kosgu': limit.kosgu,
                'year': limit.year,
                'amount': limit.amount,
                'total_contract_amount': total_contract_amount,
                'remaining_amount': remaining_amount,
            })

        # Передаем в контекст
        context['summary'] = summary
        context['page_title'] = 'Доведенные лимиты'
        context['PURCHASE_ODJ_CHOICE'] = PurchaseObject

        return context

class AddLimitView(CreateView):
    model = Limit
    form_class = LimitForm
    template_name = 'limits/add_limit.html'
    success_url = reverse_lazy('limits:limits_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        limit = form.save(commit=False)
        limit.save()
        messages.success(self.request, 'Лимит успешно создан!')
        return HttpResponseRedirect(self.success_url)

class UpdateLimitView(UpdateView):
    model = Limit
    form_class = LimitForm
    template_name = 'limits/update_limit.html'
    success_url = reverse_lazy('limits:limits_list')

    def form_valid(self, form):
        limit = form.save(commit=False)
        print(limit.kbk, limit.kosgu)
        limit.save()
        messages.success(self.request, 'Лимит успешно изменен!')
        return HttpResponseRedirect(self.success_url)

class DeleteLimitView(DeleteView):
    model = Limit
    success_url = reverse_lazy('limits:limits_list')

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Лимит удалён.')
        return super().delete(*args, **kwargs)


def get_kbk_value(kbk):
    try:
        return next(choice for choice in KBK.objects.all() if choice.code == kbk)  # Верно
    except StopIteration:
        return None

def get_kosgu_value(kosgu):
    try:
        return next(choice for choice in KOSGU.objects.all() if choice.code == str(kosgu))
    except StopIteration:
        return None


class CardLimitView(TemplateView):
    template_name = 'limits/card_limit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        kbk = self.kwargs['kbk']
        kosgu = str(self.kwargs['kosgu'])  # Приведение к строке
        year = self.kwargs['year']

        kbk_value = get_kbk_value(kbk)
        kosgu_value = get_kosgu_value(kosgu)

        # Отладочная информация
        print(f"Запрашиваемый КБК: {kbk}, полученный КБК: {kbk_value}")
        print(f"Запрашиваемый КОСГУ: {kosgu}, полученный КОСГУ: {kosgu_value}")
        print(f"Запрашиваемый год: {year}")
        # Поиск лимитов по КБК, КОСГУ и году
        limit = Limit.objects.filter(kbk__code=kbk_value, kosgu__code=kosgu_value, year=year).first()

        # Если нужно работать с одним лимитом:
        if limit:
            # Получаем первый и последний дни текущего года
            start_of_current_year = datetime(year, 1, 1)
            end_of_current_year = datetime(year, 12, 31)

            # Подсчет контрактов, соответствующих фильтрам
            contracts = Contract.objects.filter(
                kbk_type=limit.kbk,
                kosgu_type=limit.kosgu,
                contract_date__range=(start_of_current_year, end_of_current_year)
            ).distinct()

            # Также добавим контракты из декабря предыдущего года
            contracts |= Contract.objects.filter(
                kbk_type=kbk_value,
                kosgu_type=kosgu_value,
                contract_date__month=12,
                contract_date__year=year - 1
            ).distinct()

            # Расчет необходимых сумм
            total_limit_amount = limit.amount if limit else 0
            total_contract_amount = contracts.aggregate(total=models.Sum('contract_amount'))['total'] or 0.00
            total_contract_amount = Decimal(total_contract_amount)  # Приведение к Decimal

            # Рассчитываем остаток
            remaining_amount = total_limit_amount - total_contract_amount

            # Флаг для превышения лимита
            limit_exceeded = total_contract_amount > total_limit_amount

            print(f"Найдено контрактов: {contracts.count()}")

            # Подготовим контекст для шаблона
            context['contracts'] = contracts
            context['kbk'] = kbk
            context['kosgu'] = kosgu
            context['year'] = year
            context['total_limit_amount'] = total_limit_amount
            context['total_contract_amount'] = total_contract_amount
            context['remaining_amount'] = remaining_amount
            context['limit_exceeded'] = limit_exceeded

        else:
            context['contracts'] = []  # Пустой список, если лимит не найден

        return context
