from .models import ChecklistInstance, Question, Checklist
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.shortcuts import render, redirect
from .forms import ChecklistFormset
from .models import ChecklistInstance, AnsweredQuestion

from django.shortcuts import get_object_or_404


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(request, 'index.html')


# @login_rsequired
class ChecklistEntityCreate(LoginRequiredMixin, CreateView):
    model = ChecklistInstance
    fields = '__all__'


def create_book_normal(request):
    template_name = 'create_normal.html'
    heading_message = 'Model Formset Demo'
    if request.method == 'GET':
        # we don't want to display the already saved model instances
        formset = ChecklistFormset(
            queryset=AnsweredQuestion.objects.none())
    elif request.method == 'POST':
        formset = ChecklistFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            return redirect('qqq')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })
