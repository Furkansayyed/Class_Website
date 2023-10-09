from django.shortcuts import render, redirect, HttpResponse 
from .models import *
import requests
from django.conf import settings
from isodate import parse_duration
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views import generic
from .utils import *

User = get_user_model()
# Create your views here.

# @login_required(login_url='/accounts/login')
def index(request):
    # user = request.user
    # homeworks = Homework.objects.filter(user=user, is_submitted=False)
    return render(request, 'index.html')


@login_required(login_url='/accounts/login')
def getHW(request):
    user = request.user
    homeworks = Homework.objects.filter(user=user, is_submitted=False)
    return render(request, 'homework.html', {'homeworks': homeworks})


def services(request):
    return render(request, 'services.html')


def SetHomework(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        users = User.objects.filter(is_staff=False)

        for user in users:
            Homework.objects.create(
                user = user,
                subject = subject,
                title = title,
                description = desc,
                due_date = date
            )
        return redirect('/admin')
    return render(request, 'assignHW.html')

def submitHW(request, id):
    if request.method == 'POST':
        user = request.user
        print(user)
        data = request.POST
        title = data.get('title')
        subject = data.get('subject')
        
        obj = SubmittedHomeWork.objects.create(
            user=user,
            title = title,
            subject = subject,
            pdf_file = request.FILES.get('homework_pdf')
        )
        obj.save()
        Homework.objects.filter(user=user, title=title).update(is_submitted = True)
        messages.success(request, "Home Work Submitted Successfully...")
        return redirect('/submitHW')

def contact(request):
    return render(request, 'contact.html')


def youtube(request):
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    context = {
        'videos' : videos
    }
    return render(request, 'youtube.html', context)



def notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        nt = Notes.objects.create(
            user = request.user,
            title = title,
            desc = desc
        )
        nt.save()
        messages.success(request, "Notes Added Succefully....")
        return redirect("/notes")

    notes = Notes.objects.filter(user=request.user)
    return render(request, 'notes.html', {'notes': notes })

class NotesDetailsView(generic.DetailView):
    model = Notes

def details_Notes(request, id):
    notes_obj = Notes.objects.get(id=id)
    context = {'notes' : notes_obj}
    return render(request, 'notes_detail.html', context)

def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    messages.info(request, "Note Delete")
    return redirect("/notes")


def studentDiscussion(request):
    return render(request, 'dicussion.html')

@login_required(login_url='/accounts/login')
def question_list(request):
    questions = Question.objects.all().order_by("-created_at")
    return render(request, 'dicussion.html', {'questions': questions })

def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})

def post_question(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')

        obj = Question(title=title, content=content, user=user)
        obj.save()
        return redirect('/')

def post_answer(request, question_id):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content')
        question = Question.objects.get(pk=question_id)
        print(content)
        obj = Answer.objects.create(content=content, user=user, question=question)
        obj.save()
        return redirect('/dicussion')

def newsletter(request):
    if request.method == "POST":
        subject = "Thanks for Subscribing our News Letter"
        message = "Hi-Tech Classes will send you email with articles...."
        recepient = request.POST.get('news')
        send_email_to_client(subject=subject, message=message, recepient_list=recepient)
        messages.info(request, 'Thanks for subscribing our news letter....')
        return redirect('/')