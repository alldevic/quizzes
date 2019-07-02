from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.ChecklistEntityCreate.as_view()),
]
