# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import index, movies, actors, comments

urlpatterns = {
    url('index', index),
    url('movies', movies),
    url('actors', actors),
    url('comments', comments),
}

