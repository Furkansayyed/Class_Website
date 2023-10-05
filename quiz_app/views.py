from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import random
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    context = {'categories' : Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quiz/play/?category={request.GET.get('category')}")
    return render(request, 'quiz.html', context)

@login_required(login_url='/accounts/login')
def get_quiz(request):
    try:
        question_objs = Quiz_Question.objects.all()

        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains=request.GET.get('category'))

        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                'uid' : question_obj.uid,
                'category' : question_obj.category.category_name,
                'question' : question_obj.question,
                'marks': question_obj.marks,
                'answers': question_obj.get_answer()
            })


        payload = {'status' : True, 'data': data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)

    return HttpResponse("Something Went Wrong...")

@login_required(login_url='/accounts/login')
def quiz(request):
    context = {'category' : request.GET.get('category')}
    return render(request, 'play.html', context)

