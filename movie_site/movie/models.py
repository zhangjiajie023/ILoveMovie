# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class EditMixin(models.Model):
    created_by = models.ForeignKey(User, null=True, related_name='+')
    created_on = models.DateTimeField(default=timezone.now)
    changed_by = models.ForeignKey(User, null=True, related_name='+')
    changed_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Actor(EditMixin):
    name = models.CharField(max_length=256, null=False)
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER_SXE = 'OTHER'
    UNKNOWN_SEX = 'UNKNOWN'
    SEX_CHOICES = (
        (MALE, '男'),
        (FEMALE, '女'),
        (OTHER_SXE, '其他'),
        (UNKNOWN_SEX, '未知'),
    )
    sex = models.CharField(max_length=16, choices=SEX_CHOICES, default=UNKNOWN_SEX)
    birthday = models.DateField(default=timezone.now)
    country = models.CharField(max_length=64)
    description = models.TextField(null=True, max_length=4086)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def data(self):
        return {
            'name': self.name,
            'sex': self.sex,
            'birthday': str(self.birthday),
            'country': self.country,
            'description': self.description
        }


class Movie(EditMixin):
    name = models.CharField(max_length=256, null=False)
    poster = models.ImageField(null=True)
    directors = models.ManyToManyField(Actor, related_name="director_movies")
    actors = models.ManyToManyField(Actor, related_name="actor_movies")
    area = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    release_date = models.DateField(default=timezone.now)
    score = models.FloatField(default=0)
    duration = models.IntegerField(default=0)
    box_office = models.BigIntegerField(default=0)
    description = models.TextField(null=True, max_length=4086)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def directors_str(self):
        return str(self.directors)

    @property
    def actors_str(self):
        return str(self.actors)

    @property
    def data(self):
        return {
            'name': self.name,
            'directors': self.directors_str,
            'actors': self.actors_str,
            'area': self.area,
            'language': self.language,
            'type': self.type,
            'score': self.score,
            'duration': self.duration,
            'box_office': self.box_office,
            'description': self.description
        }


class Comment(EditMixin):
    user_id = models.ForeignKey(User, related_name="user_comments")
    movie_id = models.ForeignKey(Movie, related_name="movie_comments")
    content = models.TextField(default='', max_length=1024)

    @property
    def part_content(self):
        return str(self.content[:32])

    @property
    def data(self):
        return {
            'user_id': self.user_id,
            'movie_id': self.movie_id,
            'content': self.content
        }


class Favorite(EditMixin):
    user_id = models.ForeignKey(User)
    movie_id = models.ForeignKey(Movie)
