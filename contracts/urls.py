from django.urls import path

from contracts.views import PurchaseListView, PaymentDocumentListView, PaymentDocumentDetailView, \
    PaymentDocumentCreateView, PaymentDocumentUpdateView, PaymentDocumentDeleteView, IndexView

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', PurchaseListView.as_view(), name='purchase_list'),
    path('paymentdocuments/', PaymentDocumentListView.as_view(), name='paymentdocument-list'),
    path('paymentdocuments/<int:pk>/', PaymentDocumentDetailView.as_view(), name='paymentdocument-detail'),
    path('paymentdocuments/new/', PaymentDocumentCreateView.as_view(), name='paymentdocument-create'),
    path('paymentdocuments/<int:pk>/edit/', PaymentDocumentUpdateView.as_view(), name='paymentdocument-update'),
    path('paymentdocuments/<int:pk>/delete/', PaymentDocumentDeleteView.as_view(), name='paymentdocument-delete'),
]
