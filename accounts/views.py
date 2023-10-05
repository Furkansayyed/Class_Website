from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('passwd')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Username is invalid")
            return redirect('/accounts/login')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/accounts/login')
        
        else:
            login(request,user)
            return redirect('/')

    return render(request, 'login.html')

def student_register(request):
    if request.method == 'POST':
        firstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        phone_number = request.POST.get('contact')
        user_profile_pic = request.FILES.get("profile_pic")
        email= request.POST.get("email")
        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'Username already exists.....')
            return redirect('/accounts/register')
        
        user = User.objects.filter(email=email) | User.objects.filter(phone_number=phone_number)
        if user.exists():
            messages.error(request, 'Email or Contact Number already exists.....')
            return redirect('/accounts/register')
        
        user = User.objects.create(
            first_name = firstName,
            last_name = LastName,
            username = username,
            phone_number = phone_number,
            user_profile_pic = user_profile_pic,
            email = email
        )

        user.set_password(password)
        user.save()

        messages.success(request, "Account Created Successfully....")

        return redirect('/accounts/register')
    return render(request, 'register.html')

def logoutUsers(request):
    logout(request)
    return redirect('/')

def get_Users(request):
    obj = User.objects.all()
    context = {'students' : obj}
    return render(request, 'show.html', context)

@login_required(login_url='/accounts/login')
def profile(request):
    profile = User.objects.filter(username=request.user.username)
    return render(request, 'profile.html', {'profiles': profile})