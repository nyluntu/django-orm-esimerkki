# Generated by Django 4.0.2 on 2022-02-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sakila', '0004_actor_films'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
                ('language_code', models.CharField(max_length=3, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
