from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('paiment', views.about, name='about'),
    path('create', views.create, name='create'),
    path('questions', views.questions, name='questions'),
    path('program', views.program, name='program'),
]