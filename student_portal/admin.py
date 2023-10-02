from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Homework)
admin.site.register(SubmittedHomeWork)
admin.site.register(Question)
admin.site.register(Answer)
