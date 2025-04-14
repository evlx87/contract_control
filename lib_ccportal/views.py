from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import KBK, KOSGU
from .forms import KBKForm, KOSGUForm
from django.contrib.auth.mixins import LoginRequiredMixin

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