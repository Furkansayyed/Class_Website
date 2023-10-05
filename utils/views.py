from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()


# Create your views here.
def todo(request):
    if request.method == 'POST':
        user = request.user;
        title = request.POST.get('title')
        obj = Todo.objects.create(user=user, title=title)
        obj.save()
        messages.info(request, "Todo Addes Succesfully...")
        return redirect("/utils/todo")
    todo = Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todos_done = True

    else:
        todos_done = False
    context = {
        'todos':todo,
            'todos_done':todos_done
        }

    return render(request,"todo.html", context)

def update_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
        messages.info(request, f"{todo.title} is unmarked" )

    else:
        todo.is_finished = True
        messages.success(request, f"{todo.title} is marked finished" )

    todo.save()
    return redirect('/utils/todo')


def delete_todo(request, pk=None):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.info(request, f"{todo.title} is Deletd" )
    return redirect('/utils/todo')

@login_required(login_url="/accounts/login")
def show_models(request):
    obj = ModelCategory.objects.all()
    return render(request, 'categories.html', {'categories' : obj})    

@login_required(login_url="/accounts/login")
def ModelDetail(request, category):
    obj = PhysicsModels.objects.filter(category=category)
    return render(request, 'pmodels.html', {'pmodels': obj})

@login_required(login_url="/accounts/login")
def ModelViews(request, id):
    obj = PhysicsModels.objects.filter(id=id)
    return render(request, 'mode_view.html', {'pmodels' : obj})