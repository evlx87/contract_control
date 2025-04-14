from django.urls import path

from lib_ccportal.views import KBKListView, KBKCreateView, KBKUpdateView, KBKDeleteView, KOSGUListView, KOSGUCreateView, \
    KOSGUUpdateView, KOSGUDeleteView

app_name = 'lib_ccportal'

urlpatterns = [
    # KBK URLs
    path('kbk/', KBKListView.as_view(), name='kbk_list'),
    path('kbk/add/', KBKCreateView.as_view(), name='kbk_add'),
    path('kbk/edit/<int:pk>/', KBKUpdateView.as_view(), name='kbk_edit'),
    path('kbk/delete/<int:pk>/', KBKDeleteView.as_view(), name='kbk_delete'),
    # KOSGU URLs
    path('kosgu/', KOSGUListView.as_view(), name='kosgu_list'),
    path('kosgu/add/', KOSGUCreateView.as_view(), name='kosgu_add'),
    path('kosgu/edit/<int:pk>/', KOSGUUpdateView.as_view(), name='kosgu_edit'),
    path('kosgu/delete/<int:pk>/', KOSGUDeleteView.as_view(), name='kosgu_delete'),
]