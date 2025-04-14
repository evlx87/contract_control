from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View

from contracts.models import Contract
from .forms import KBKForm, KOSGUForm
from .models import KBK, KOSGU


# Create your views here.
# Список KBK
class KBKListView(LoginRequiredMixin, ListView):
    model = KBK
    template_name = 'lib_ccportal/kbk_list.html'
    context_object_name = 'kbk_list'

# Добавление KBK
class KBKCreateView(LoginRequiredMixin, CreateView):
    model = KBK
    form_class = KBKForm
    template_name = 'lib_ccportal/kbk_form.html'
    success_url = reverse_lazy('lib_ccportal:kbk_list')

# Редактирование KBK
class KBKUpdateView(LoginRequiredMixin, UpdateView):
    model = KBK
    form_class = KBKForm
    template_name = 'lib_ccportal/kbk_form.html'
    success_url = reverse_lazy('lib_ccportal:kbk_list')

# Удаление KBK
class KBKDeleteView(LoginRequiredMixin, View):
    template_name = 'lib_ccportal/kbk_delete.html'

    def get(self, request, pk):
        kbk = get_object_or_404(KBK, pk=pk)
        # Проверяем связанные контракты
        related_contracts = Contract.objects.filter(kbk_type=kbk)
        context = {
            'kbk': kbk,
            'related_contracts': related_contracts,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        kbk = get_object_or_404(KBK, pk=pk)
        # Проверяем связанные контракты
        related_contracts = Contract.objects.filter(kbk_type=kbk)
        if related_contracts.exists():
            messages.error(request, 'Нельзя удалить КБК, так как к нему привязаны контракты.')
            return redirect('lib_ccportal:kbk_list')
        # Удаляем, если контрактов нет
        kbk.delete()
        messages.success(request, f'КБК "{kbk.code}" успешно удален.')
        return redirect('lib_ccportal:kbk_list')

# Список KOSGU
class KOSGUListView(LoginRequiredMixin, ListView):
    model = KOSGU
    template_name = 'lib_ccportal/kosgu_list.html'
    context_object_name = 'kosgu_list'

# Добавление KOSGU
class KOSGUCreateView(LoginRequiredMixin, CreateView):
    model = KOSGU
    form_class = KOSGUForm
    template_name = 'lib_ccportal/kosgu_form.html'
    success_url = reverse_lazy('lib_ccportal:kosgu_list')

# Редактирование KOSGU
class KOSGUUpdateView(LoginRequiredMixin, UpdateView):
    model = KOSGU
    form_class = KOSGUForm
    template_name = 'lib_ccportal/kosgu_form.html'
    success_url = reverse_lazy('lib_ccportal:kosgu_list')

# Удаление KOSGU
class KOSGUDeleteView(LoginRequiredMixin, View):
    template_name = 'lib_ccportal/kosgu_delete.html'

    def get(self, request, pk):
        kosgu = get_object_or_404(KOSGU, pk=pk)
        # Проверяем связанные контракты
        related_contracts = Contract.objects.filter(kosgu_type=kosgu)
        context = {
            'kosgu': kosgu,
            'related_contracts': related_contracts,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        kosgu = get_object_or_404(KOSGU, pk=pk)
        # Проверяем связанные контракты
        related_contracts = Contract.objects.filter(kosgu_type=kosgu)
        if related_contracts.exists():
            messages.error(request, 'Нельзя удалить КОСГУ, так как к нему привязаны контракты.')
            return redirect('lib_ccportal:kosgu_list')
        # Удаляем, если контрактов нет
        kosgu.delete()
        messages.success(request, f'КОСГУ "{kosgu.code}" успешно удален.')
        return redirect('lib_ccportal:kosgu_list')