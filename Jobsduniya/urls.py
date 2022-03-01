from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('jobspage/',views.jobspage,name="jobspage"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    # path('services/',views.services,name="services"),
    path('postjob/',views.postjob,name="postjob"),
    path('search/',views.search,name="search"),
]