from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('todo', views.todo, name="addtodo"),
    path('update_todo/<int:pk>', views.update_todo, name="update-todo"),
    path('delete_todo/<int:pk>', views.delete_todo, name="delete-todo"),

    path('modelcategories', views.show_models, name="displaymodels"),
    path('pmodeldetails/<category>', views.ModelDetail, name="showpmodels"),
    path('viewmodels/<id>', views.ModelViews, name="displaymodels"),
]