from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(request, 'index.html')
