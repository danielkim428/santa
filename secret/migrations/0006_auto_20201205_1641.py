# Generated by Django 3.0.3 on 2020-12-05 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secret', '0005_group_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mortal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='angel_of', to=settings.AUTH_USER_MODEL),
        ),
    ]