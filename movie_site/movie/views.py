# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Movie, Actor, Comment


def index(request):
    return render(request, 'movie/index.html', {})


def movies(request):
    all = Movie.objects.all()
    data = []
    for one in all:
        data.append(one.data)
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def actors(request):
    all = Actor.objects.all()
    data = []
    for one in all:
        data.append(one.data)
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def comments(request):
    user_id = request.GET.get('user_id')
    movie_id = request.GET.get('movie_id')

    query = Comment.objects
    if user_id:
        query = query.filter(user_id=user_id)
    if movie_id:
        query = query.filter(user_id=movie_id)
    query = query.order_by('changed_on')

    data = []
    for one in query.all():
        data.append(one.data)
    return HttpResponse(json.dumps(data, ensure_ascii=False))

