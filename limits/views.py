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
        return next(choice[0] for choice in KOSGU_TYPE_CHOICES if choice[1] == kosgu)
    except StopIteration:
        return None


class CardLimitView(TemplateView):
    template_name = 'limits/card_limit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем значения КБК и КОСГУ из URL
        kbk = self.kwargs['kbk']
        kosgu = self.kwargs['kosgu']

        # Преобразуем значения КБК и КОСГУ в строки, подходящие для поиска по полю CharField
        kbk_value = get_kbk_value(kbk)
        kosgu_value = get_kosgu_value(kosgu)

        # Если найдены соответствия, выполняем поиск контрактов
        if kbk_value is not None and kosgu_value is not None:
            contracts = Contract.objects.filter(kbk_type=kbk_value, kosgu_type=kosgu_value)
        else:
            contracts = []

        # Добавляем контракты в контекст
        context['contracts'] = contracts

        return context