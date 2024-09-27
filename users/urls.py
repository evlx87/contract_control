from django.urls import path
from .views import user_login, user_logout

app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]
