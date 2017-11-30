# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class EditMixin(models.Model):
    created_by = models.ForeignKey(User, related_name='+')
    created_on = models.DateTimeField(default=timezone.now)
    changed_by = models.ForeignKey(User, related_name='+')
    changed_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Movie(EditMixin):
    name = models.CharField(max_length=256)
    poster = models.ImageField
    director = models.CharField(max_length=128)
    area = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    release_date = models.DateField
    score = models.FloatField
    duration = models.IntegerField
    box_office = models.BigIntegerField
    description = models.TextField

    def __str__(self):
        return self.name


class Actor(EditMixin):
    name = models.CharField(max_length=256)
    sex = models.CharField(max_length=16)
    birthday = models.DateField
    country = models.CharField(max_length=64)
    description = models.TextField
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name


class Comment(EditMixin):
    user_id = models.ForeignKey(User, related_name='+')
    movie_id = models.ForeignKey(Movie)
    content = models.TextField


class Favorite(EditMixin):
    user_id = models.ForeignKey(User)
    movie_id = models.ForeignKey(Movie)