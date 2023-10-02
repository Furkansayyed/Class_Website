from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="getquiz"),
    path('api/get-quiz/', views.get_quiz, name='quizApi'),
    path('play/', views.quiz, name='play_quiz'),
]