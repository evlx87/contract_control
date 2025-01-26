from django.urls import path

from users.views import custom_login_view

app_name = 'users'

urlpatterns = [
    path('login/', custom_login_view, name='login'),
]

