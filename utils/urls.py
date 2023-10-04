from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('todo', views.todo, name="addtodo"),
    path('update_todo/<int:pk>', views.update_todo, name="update-todo"),
    path('delete_todo/<int:pk>', views.delete_todo, name="delete-todo"),
]