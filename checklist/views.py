from .models import ChecklistInstance, Question
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(request, 'index.html')


class ChecklistEntityCreate(CreateView):
    model = Question
    fields = '__all__'


class ChecklistEntityUpdate(UpdateView):
    model = ChecklistInstance
    fields = '__all__'


class ChecklistEntityDelete(DeleteView):
    model = ChecklistInstance
    success_url = reverse_lazy('authors')
