from django.shortcuts import render
from .models import Limit


# Create your views here.
def limit_card(request):
    limit_data = Limit.objects.all()  # Получаем все данные из модели Limit
    return render(request,
                  'limits/limits_card.html',
                  {'limit_data': limit_data})
