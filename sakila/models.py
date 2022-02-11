from django.db import models

# Create your models here.
class Film(models.Model):

    film_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=1024)
    length = models.IntegerField()
    release_date = models.DateField()

class Actor(models.Model):

    actor_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    last_modified = models.DateTimeField(auto_now=True)