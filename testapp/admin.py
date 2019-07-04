from django.contrib import admin
from .models import Answer, Question, Quiz, QuizInstance
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionInline(admin.TabularInline):
    model = Question


class QuizInline(admin.TabularInline):
    model = Quiz


class QuizInstanceInline(admin.TabularInline):
    model = QuizInstance


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuizInstanceInline]


@admin.register(QuizInstance)
class QuizInstanceAdmin(admin.ModelAdmin):
    pass
