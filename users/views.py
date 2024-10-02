import logging

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

logger = logging.getLogger(__name__)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info(f"Пользователь {username} успешно вошел в систему")
            return redirect('contracts:index')
        else:
            logger.warning(
                f"Неудачная попытка входа пользователя с именем {username}")
            # Обработка ошибки неверных учетных данных
            pass
    return render(request, 'users/login.html')


def user_logout(request):
    logger.info(f"Пользователь {request.user.username} вышел из системы")
    logout(request)
    return redirect('contracts:index')
