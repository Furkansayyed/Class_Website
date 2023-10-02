from django.contrib import admin
from .models import *
# Register your models here.

class ShowStudents(admin.ModelAdmin):
    list_display= ('username', 'first_name', 'phone_number', 'email', )

admin.site.register(MyStudents, ShowStudents)