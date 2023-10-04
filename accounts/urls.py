from django.urls import path
from . import views

urlpatterns = [
    path('login', views.student_login, name="studetnlogin"),
    path('register', views.student_register, name='studentregister'),
    path('logout', views.logoutUsers, name='logoutstudents'),
]
