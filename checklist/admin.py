from django.contrib import admin
from .models import Car, Platform, ChecklistType, Answer, Question, AnswerType, Checklist, Staff, ChecklistEntity

# Register your models here.
admin.site.register(Car)
admin.site.register(Platform)
admin.site.register(ChecklistType)
admin.site.register(AnswerType)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Checklist)
admin.site.register(Staff)
admin.site.register(ChecklistEntity)
