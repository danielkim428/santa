# Generated by Django 3.0.3 on 2020-12-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0009_auto_20201205_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='content',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]
