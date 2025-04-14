from django.urls import path
from . import views

app_name = 'lib_ccportal'

urlpatterns = [
    # KBK URLs
    path('kbk/', views.KBKListView.as_view(), name='kbk_list'),
    path('kbk/add/', views.KBKCreateView.as_view(), name='kbk_add'),
    path('kbk/edit/<int:pk>/', views.KBKUpdateView.as_view(), name='kbk_edit'),

    # KOSGU URLs
    path('kosgu/', views.KOSGUListView.as_view(), name='kosgu_list'),
    path('kosgu/add/', views.KOSGUCreateView.as_view(), name='kosgu_add'),
    path('kosgu/edit/<int:pk>/', views.KOSGUUpdateView.as_view(), name='kosgu_edit'),
]