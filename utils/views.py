from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def todo(request):
    return HttpResponse("<h3?> Weclome to Utils </h3?")