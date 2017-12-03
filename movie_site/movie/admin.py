from django.contrib import admin
from .models import Movie, Actor, Comment


class SaveModelMixin(object):
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        obj.changed_by = request.user
        obj.save()


class MovieAdmin(admin.ModelAdmin, SaveModelMixin):
    fields = ['name', 'poster', 'directors', 'actors', 'area', 'type', 'score',
              'release_date', 'box_office', 'is_deleted']
    list_display = ('name', 'directors_str', 'area', 'type', 'score', 'release_date')

admin.site.register(Movie, MovieAdmin)


class ActorAdmin(admin.ModelAdmin, SaveModelMixin):
    fields = ['name', 'picture', 'sex', 'birthday', 'country', 'description',
              'is_deleted']
    list_display = ('name', 'sex', 'birthday', 'country')

admin.site.register(Actor, ActorAdmin)


class CommentAdmin(admin.ModelAdmin, SaveModelMixin):
    fields = ['user', 'movie', 'content']
    list_display = ('user', 'movie', 'part_content')

admin.site.register(Comment, CommentAdmin)
