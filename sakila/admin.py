from django.contrib import admin

from sakila.models import Film, Actor, FilmLanguage

# Register your models here.
admin.site.register(Film)
admin.site.register(FilmLanguage)
admin.site.register(Actor)
