from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from contracts.models import Contract
from .choice_objects import PURCHASE_ODJ_CHOICE, KBK_TYPE_CHOICES, KOSGU_TYPE_CHOICES
from .forms import LimitForm
from .models import Limit


class LimitListView(ListView):
    model = Limit
    template_name = 'limits/limits_list.html'
    context_object_name = 'limits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Доведенные лимиты'
        context['PURCHASE_ODJ_CHOICE'] = PURCHASE_ODJ_CHOICE
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
        return next(choice[0] for choice in KBK_TYPE_CHOICES if choice[1] == kbk)
    except StopIteration:
        return None


def get_kosgu_value(kosgu):
    try:
        return next(choice[0] for choice in KOSGU_TYPE_CHOICES if choice[0] == str(kosgu))  # Приводим к строке
    except StopIteration:
        return None


class CardLimitView(TemplateView):
    template_name = 'limits/card_limit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        kbk = self.kwargs['kbk']
        kosgu = str(self.kwargs['kosgu'])  # Приведение к строке

        kbk_value = get_kbk_value(kbk)
        kosgu_value = get_kosgu_value(kosgu)

        # Отладочная информация
        print(f"Запрашиваемый КБК: {kbk}, полученный КБК: {kbk_value}")
        print(f"Запрашиваемый КОСГУ: {kosgu}, полученный КОСГУ: {kosgu_value}")

        # Поиск контрактов
        contracts = Contract.objects.filter(kbk_type=kbk_value, kosgu_type=kosgu_value)

        print(f"Найдено контрактов: {contracts.count()}")  # Выводим количество найденных контрактов

        context['contracts'] = contracts
        context['kbk'] = kbk
        context['kosgu'] = kosgu

        return context
