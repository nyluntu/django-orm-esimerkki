from django.contrib import admin

from sakila.models import Film, Actor

# Register your models here.
admin.site.register(Film)
admin.site.register(Actor)
