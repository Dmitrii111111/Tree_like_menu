from django.http import HttpResponseNotFound
from django.shortcuts import render


def base(request, name):
    return render(request, 'menu/home.html', {'name': name})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
