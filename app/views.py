from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse ('home'),
        'Показать текущее время': reverse ('time'),
        'Показать содержимое рабочей директории': reverse ('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    names = ', '.join(os.listdir('/Users/Ilya/Desktop/Питонство/Django/project_1'))
    return HttpResponse(names)