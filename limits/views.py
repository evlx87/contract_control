from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView

from .forms import LimitForm
from .models import Limit


class LimitCardView(TemplateView):
    model = Limit
    template_name = 'limits/limits_card.html'
    context_object_name = 'limits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Доведенные лимиты'
        return context

class AddLimitView(CreateView):
    model = Limit
    form_class = LimitForm
    template_name = 'limits/add_limit.html'
    success_url = '/limits/'

    def form_valid(self, form):
        limit = form.save(commit=False)
        limit.save()
        messages.success(self.request, 'Лимит успешно создан!')
        return HttpResponseRedirect(self.success_url)

class UpdateLimitView(UpdateView):
    model = Limit
    form_class = LimitForm
    template_name = 'limits/update_limit.html'
    success_url = '/limits/'

    def form_valid(self, form):
        limit = form.save(commit=False)
        limit.save()
        messages.success(self.request, 'Лимит успешно изменен!')
        return HttpResponseRedirect(self.success_url)

class DeleteLimitView(DeleteView):
    model = Limit
    success_url = '/limits/'

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Лимит удалён.')
        return super().delete(*args, **kwargs)