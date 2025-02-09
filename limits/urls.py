from django.urls import path

from limits.views import AddLimitView, LimitListView, CardLimitView, UpdateLimitView, DeleteLimitView

app_name = 'limits'

urlpatterns = [
    path('limits-list/', LimitListView.as_view(), name='limits_list'),
    path('add-limit/', AddLimitView.as_view(), name='add_limit'),
    path('card_limit/<path:kbk>/<int:kosgu>/<int:year>/', CardLimitView.as_view(), name='card_limit'),
    path('<int:pk>/edit/', UpdateLimitView.as_view(), name='update_limit'),  # Редактирование
    path('<int:pk>/delete/', DeleteLimitView.as_view(), name='delete_limit'),  # Удаление
]

