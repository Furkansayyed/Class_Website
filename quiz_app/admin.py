from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)


class QuizAnswerAdmin(admin.StackedInline):
    model = Quiz_Answer

class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = [QuizAnswerAdmin]

admin.site.register(Quiz_Question, QuizQuestionAdmin)
admin.site.register(Quiz_Answer)