# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import User, Movie, Actor, Comment
from .utils import json_data


def index(request):
    return render(request, 'movie/index.html', {})


def get_movies(request):
    all = Movie.objects.all()
    data = []
    for one in all:
        data.append(one.data)
    return HttpResponse(json_data(data))


def get_actors(request):
    all = Actor.objects.all()
    data = []
    for one in all:
        data.append(one.data)
    return HttpResponse(json_data(data))


def get_comments(request):
    """
    ./comments/?user_id=xxx&movie_id=xxx
    :param request:
    :return:
    """
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
    return HttpResponse(json_data(data))


def get_users(request):
    """
    ./users/?user_id=xxx
    ./users/?username=xxx
    :param request:
    :return:
    """
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    if user_id:
        user = User.objects.filter(id=user_id).one()
        return HttpResponse(json_data(user.data))
    elif username:
        user = User.objects.filter(username__contains=username).one()
        return HttpResponse(json_data(user.data))
    else:
        raise Exception('Need args for /users/')
