from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    assigned_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    is_submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " HomeWork"

class SubmittedHomeWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='homework_pdfs/', null=True)
    submit_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} by {self.user}'

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content
    
class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

