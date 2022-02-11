from pyexpat import model
from django.db import models

# Create your models here.
class FilmLanguage(models.Model):

    language = models.CharField(max_length=30)
    language_code = models.CharField(max_length=3, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.language

class Film(models.Model):

    film_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1024)
    length = models.IntegerField()
    release_date = models.DateField()
    language = models.ForeignKey(FilmLanguage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Actor(models.Model):

    actor_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    last_modified = models.DateTimeField(auto_now=True)

    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.first_name + " " + self.last_name

