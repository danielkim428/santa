# Generated by Django 3.0.3 on 2020-12-05 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0002_profile_mortal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='woodstock',
        ),
    ]
