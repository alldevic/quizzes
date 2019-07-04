from django.contrib import admin
from .models import Car, AnswerType, Answer, FilledChecklistInstance, Platform
from .models import Checklist, ChecklistInstance, ChecklistType, Question, Staff
from .models import AnsweredQuestion

# Register your models here.


@admin.register(AnswerType)
class AnswerTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('label', 'type')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('reg_id', 'model')


@admin.register(ChecklistInstance)
class ChecklistInstanceAdmin(admin.ModelAdmin):
    list_display = ('checklist', 'staff', 'car', 'platform', 'date', 'time')


@admin.register(ChecklistType)
class ChecklistTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('label', 'type')


@admin.register(FilledChecklistInstance)
class FilledChecklistInstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


@admin.register(AnsweredQuestion)
class AnsweredQuestion(admin.ModelAdmin):
    pass
