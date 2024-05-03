from django.urls import path, re_path

from contracts.views import PurchaseListView, IndexView, AddContractView, contract_detail, AddPaymentDocView, \
    AddPaymentOrderView

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', PurchaseListView.as_view(), name='purchase_list'),
    path('add/', AddContractView.as_view(), name='add_contract'),
    path('contract/<int:pk>/', contract_detail, name='contract-detail'),
    path('add_doc/<int:contract_id>/', AddPaymentDocView.as_view(), name='add_payment_doc'),
    path('add_order/<int:contract_id>/', AddPaymentOrderView.as_view(), name='add_payment_order')
]
