from django.contrib import admin
from .models import Car, AnswerType, Answer, FilledChecklistEntity, Platform
from .models import Checklist, ChecklistEntity, ChecklistType, Question, Staff

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


class ChecklistEntityInline(admin.TabularInline):
    model = ChecklistEntity


@admin.register(ChecklistEntity)
class ChecklistEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(ChecklistType)
class ChecklistTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    inlines = [ChecklistEntityInline]


@admin.register(FilledChecklistEntity)
class FilledChecklistEntityAdmin(admin.ModelAdmin):
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
