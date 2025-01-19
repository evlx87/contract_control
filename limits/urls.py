from django.urls import path
from limits.views import AddLimitView, LimitListView, CardLimitView

app_name = 'limits'

urlpatterns = [
    path('limits-list/', LimitListView.as_view(), name='limits_list'),
    path('add-limit/', AddLimitView.as_view(), name='add_limit'),
    path('card_limit/<path:kbk>/<int:kosgu>/<int:year>/', CardLimitView.as_view(), name='card_limit')
]

