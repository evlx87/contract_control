from django.urls import path

from contracts.views import PurchaseListView, IndexView, AddContractView, contract_detail, AddPaymentDocView, \
    add_payment_document

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', PurchaseListView.as_view(), name='purchase_list'),
    path('add/', AddContractView.as_view(), name='add_contract'),
    path('contracts/<str:contract_number>/', contract_detail, name='contract-detail'),
    path('add_doc/<int:contract_id>/', AddPaymentDocView.as_view(), name='add_payment_doc'),
    # path('add_doc/<int:contract_id>/', add_payment_document, name='add_doc'),
]
