from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index, name="indexPage"),
    path('contact', views.contact, name="contactPage"),
    path('services', views.services, name="services"),
    path('youtube', views.youtube, name='videos'),


    path('assignhw', views.SetHomework, name='AssignHomework'),
    path('submitHomework/<id>', views.submitHW, name="submitHomwework"),
    path('dicussion', views.question_list, name='dicussion'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('ask_auestion', views.post_question, name='ask_question'),
    path('post_answer/<int:question_id>', views.post_answer, name="post_answer")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()