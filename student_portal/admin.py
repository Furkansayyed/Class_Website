from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Homework)

class SHAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'pdf_file', 'submit_date')

admin.site.register(SubmittedHomeWork, SHAdmin)
admin.site.register(Question)
admin.site.register(Answer)
