from django.urls import path
from limits.views import AddLimitView, LimitListView

app_name = 'limits'

urlpatterns = [
    path('limit-list/', LimitListView.as_view(), name='limit_list'),
    path('add-limit/', AddLimitView.as_view(), name='add_limit'),
]

