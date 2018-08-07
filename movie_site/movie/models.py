# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, AbstractBaseUser
from django.db import models
from django.db.models import deletion
import django.utils.timezone as timezone


# class User(AbstractBaseUser):
#     username = models.CharField(max_length=128, unique=True)
#     email = models.EmailField(blank=True, null=True)
#     telephone = models.CharField(max_length=16, blank=True, null=True)
#     is_admin = models.BooleanField('Can visit /admin', default=False)
#     is_superuser = models.BooleanField('Has all permissions', default=False)


class EditMixin(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='+',
                                   on_delete=deletion.SET(None))
    created_on = models.DateTimeField(default=timezone.now)
    changed_by = models.ForeignKey(User, blank=True, null=True, related_name='+',
                                   on_delete=deletion.SET(None))
    changed_on = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Actor(EditMixin):
    name = models.CharField(max_length=256)
    picture = models.ImageField(blank=True, null=True)
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
    country = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(max_length=4086, blank=True, null=True)
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
    name = models.CharField(max_length=256)
    poster = models.ImageField(blank=True, null=True)
    directors = models.ManyToManyField(Actor, related_name="director_movies")
    actors = models.ManyToManyField(Actor, related_name="actor_movies")
    area = models.CharField(max_length=64, blank=True, null=True)
    language = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    release_date = models.DateField(default=timezone.now)
    score = models.FloatField(default=0)
    duration = models.IntegerField(default=0)
    box_office = models.BigIntegerField(default=0)
    description = models.TextField(max_length=4086, blank=True, null=True)
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
    user = models.ForeignKey(User, related_name="user_comments")
    movie = models.ForeignKey(Movie, related_name="movie_comments")
    content = models.TextField(default='', max_length=4086)

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
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
