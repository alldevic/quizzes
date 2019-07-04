from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.ChecklistEntityCreate.as_view()),
    path('qqq/', views.create_book_normal, name='qqq'),

]
