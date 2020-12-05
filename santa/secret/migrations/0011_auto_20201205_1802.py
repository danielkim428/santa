# Generated by Django 3.0.3 on 2020-12-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0010_auto_20201205_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='title',
        ),
        migrations.AddField(
            model_name='letter',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='letters',
            field=models.ManyToManyField(to='secret.Letter'),
        ),
    ]
