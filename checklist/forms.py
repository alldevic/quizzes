from django.forms.models import BaseInlineFormSet
from django.forms.models import inlineformset_factory
from django import forms
from django.forms import inlineformset_factory

from .models import Checklist, Question, Answer, AnsweredQuestion, ChecklistInstance

ChecklistFormset = inlineformset_factory(
    ChecklistInstance, AnsweredQuestion, fields="__all__")
