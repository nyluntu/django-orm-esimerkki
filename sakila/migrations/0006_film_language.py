# Generated by Django 4.0.2 on 2022-02-11 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sakila', '0005_filmlanguage'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sakila.filmlanguage'),
        ),
    ]
