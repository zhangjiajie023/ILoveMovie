from django.contrib import admin
from .models import Movie, Actor, Comment


class MovieAdmin(admin.ModelAdmin):
    fields = ['name', 'poster', 'director', 'area', 'type', 'score',
              'release_date', 'box_office']
    list_display = ('name', 'director', 'area', 'type', 'score', 'release_date')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Comment)
