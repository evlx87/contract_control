from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from contracts.forms import PaymentDocumentForm, ContractForm
from contracts.models import Contract, PaymentDocument


# Create your views here.
class IndexView(TemplateView):
    template_name = 'contracts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Hello, world!"
        return context


def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contracts/')  # Перенаправление на главную страницу после добавления, измените это по надобности
    else:
        form = ContractForm()
    return render(request, 'contracts/purchase_add.html', {'form': form})


class PurchaseListView(ListView):
    model = Contract
    template_name = 'contracts/purchases_list.html'  # Указываем имя шаблона
    context_object_name = 'purchases'  # Как будет называться переменная в шаблоне


class PaymentDocumentListView(ListView):
    model = PaymentDocument
    template_name = 'contracts/paymentdocument_list.html'
    context_object_name = 'documents'


class PaymentDocumentDetailView(DetailView):
    model = PaymentDocument
    template_name = 'contracts/paymentdocument_detail.html'
    context_object_name = 'document'


class PaymentDocumentCreateView(CreateView):
    model = PaymentDocument
    form_class = PaymentDocumentForm
    template_name = 'contracts/paymentdocument_form.html'

    def get_success_url(self):
        return reverse_lazy('paymentdocument-detail', kwargs={'pk': self.object.pk})


class PaymentDocumentUpdateView(UpdateView):
    model = PaymentDocument
    form_class = PaymentDocumentForm
    template_name = 'contracts/paymentdocument_form.html'

    def get_success_url(self):
        return reverse_lazy('paymentdocument-detail', kwargs={'pk': self.object.pk})


class PaymentDocumentDeleteView(DeleteView):
    model = PaymentDocument
    template_name = 'contracts/paymentdocument_confirm_delete.html'
    success_url = reverse_lazy('paymentdocument-list')
