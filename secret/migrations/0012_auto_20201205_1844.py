# Generated by Django 3.0.3 on 2020-12-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0011_auto_20201205_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='letters',
            field=models.ManyToManyField(blank=True, to='secret.Letter'),
        ),
    ]
