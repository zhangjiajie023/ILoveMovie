# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index),
    url('index/', views.index),
    url('movies/', views.get_movies),
    url('actors/', views.get_actors),
    url('comments/', views.get_comments),
]

