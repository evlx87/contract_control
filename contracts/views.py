import io
import logging

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView
from openpyxl.utils import get_column_letter
from openpyxl.workbook import Workbook

from contracts.forms import ContractForm, PaymentDocumentForm, PaymentOrderForm
from contracts.models import Contract

logger = logging.getLogger(__name__)


# Create your views here.
class IndexView(TemplateView):
    template_name = 'contracts/index.html'
    login_url = 'registration:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная'

        if self.request.user.is_authenticated:
            context['username'] = self.request.user.username

        return context


class AddContractView(View):
    def get(self, request):
        form = ContractForm()
        logger.info("Страница добавления контракта была загружена")
        return render(request, 'contracts/purchase_add.html', {'form': form})

    def post(self, request):
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Контракт успешно добавлен')
            logger.info("Контракт успешно сохранен")
            return redirect('/contracts/')
        else:
            logger.error("Форма контракта не валидна: %s", form.errors)
            messages.error(request, 'Ошибка при добавлении контракта. Проверьте введенные данные')
            return render(request, 'contracts/purchase_add.html', {'form': form})


class PurchaseListView(ListView):
    model = Contract
    template_name = 'contracts/purchases_list.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(service_end_date__year=year)
        subject = self.request.GET.get('subject')
        if subject:
            queryset = queryset.filter(service_end_date=subject)
        return queryset.order_by('service_end_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Закупки'
        # context['years'] = Contract.objects.order_by('contract_date').dates('contract_date', 'year', order='ASC')
        context['years'] = Contract.objects.order_by('service_end_date').dates('service_end_date', 'year', order='ASC')
        context['selected_year'] = self.request.GET.get('year', '')
        context['subjects'] = Contract.objects.values_list('contract_subject', flat=True).distinct()
        context['selected_subject'] = self.request.GET.get('subject', '')
        return context


def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request,
                  'contracts/contract_detail.html',
                  {'contract_detail': contract})


def contract_edit(request, contract_id):
    contract = Contract.objects.get(pk=contract_id)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)

        if form.is_valid():
            if 'contract_file' in request.FILES:
                contract.contract_file = request.FILES['contract_file']

            form.save()
            logger.info(f"Контракт с ID {contract.id} успешно отредактирован")
            return redirect('contract-detail', pk=contract.id)
    else:
        form = ContractForm(instance=contract)

    return render(request, 'contracts/contract_edit.html',
                  {'form': form, 'contract': contract})


def contract_delete(request, pk):
    contract = Contract.objects.get(pk=pk)
    if request.method == 'POST':
        contract.delete()
        messages.success(request, 'Данные о закупке были успешно удалены.')
        logger.info(f"Контракт с ID {pk} был удален")
        return redirect('contracts:purchase_list')

    return render(request,
                  'contracts/contract_delete.html',
                  {'contract': contract})


class AddPaymentDocView(View):
    template_name = 'contracts/payment_doc_add.html'

    def get_contract(self, contract_id):
        return get_object_or_404(Contract, id=contract_id)

    def get(self, request, contract_id=None):
        contract = None
        if contract_id:
            contract = self.get_contract(contract_id)
            form = PaymentDocumentForm(initial={'contract': contract})
        else:
            form = PaymentDocumentForm()
        logger.info('Запрошена страница для добавления документа оплаты')
        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})

    def post(self, request, contract_id):
        contract = self.get_contract(contract_id)
        form = PaymentDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            payment_document = form.save(commit=False)
            payment_document.contract = contract
            payment_document.save()
            logger.info(f"Создан новый документ оплаты для контракта с ID {contract_id}")
            return redirect(
                'contracts:contract-detail',
                # contract_number=contract.contract_number)
                pk=contract.id)
        else:
            logger.warning('Форма документа оплаты содержит ошибки')

        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})


class AddPaymentOrderView(View):
    template_name = 'contracts/payment_order_add.html'

    def get(self, request, contract_id=None):
        contract = get_object_or_404(Contract, id=contract_id)
        form = PaymentOrderForm(initial={'contract': contract})
        logger.info(f"Отображена страница для добавления платежного поручения для контракта с ID {contract_id}")
        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})

    def post(self, request, contract_id):
        contract = get_object_or_404(Contract, id=contract_id)
        form = PaymentOrderForm(request.POST, request.FILES)
        if form.is_valid():
            payment_order = form.save(commit=False)
            payment_order.contract = contract
            payment_order.save()
            logger.info(f"Создано новое платежное поручение для контракта с ID {contract_id}")
            return redirect(
                'contracts:contract-detail',
                # contract_number=contract.contract_number)
                pk = contract.id)
        else:
            logger.warning('Форма платежного поручения содержит ошибки')

        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})

class JournalListView(ListView):
    model = Contract
    template_name = 'contracts/journal_list.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('contract_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Журнал регистрации контрактов'
        return context


# Представление для экспорта в Excel
def export_to_excel(request):
    purchases = Contract.objects.all().order_by('-id')  # Получение всех объектов модели контракта

    # Данные для заполнения таблицы
    data = [['Дата контракта', 'Номер контракта', 'Контрагент', 'Предмет контракта',
             'Срок действия контракта', 'Дата начала услуг/поставки', 'Дата окончания услуг/поставки',
             'Сумма контракта', 'Тип закупки']]

    for purchase in purchases:
        data.append([
            purchase.contract_date.strftime('%d.%m.%Y'),
            purchase.contract_number,
            purchase.supplier,
            purchase.contract_subject,
            purchase.contract_duration.strftime('%d.%m.%Y'),
            purchase.service_start_date.strftime('%d.%m.%Y'),
            purchase.service_end_date.strftime('%d.%m.%Y'),
            purchase.contract_amount,
            purchase.purchase_type
        ])

    # Создание новой рабочей книги
    wb = Workbook()
    ws = wb.active

    # Заполнение данными
    for row in data:
        ws.append(row)

    # Установка ширины колонок
    dim_holder = {}
    for col in range(len(data[0])):
        for row in range(1, len(data) + 1):
            column_letter = get_column_letter(col + 1)
            cell_value = str(ws.cell(row=row, column=col + 1).value)
            try:
                dim_holder[column_letter].append(len(cell_value))
            except KeyError:
                dim_holder[column_letter] = [len(cell_value)]

    for col, widths in dim_holder.items():
        max_width = max(widths)
        ws.column_dimensions[col].width = max_width + 3

    # Сохранение файла в память
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    # Отправка файла пользователю
    response = HttpResponse(
        content=output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename="journal.xlsx"'
    return response