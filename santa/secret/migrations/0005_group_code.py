# Generated by Django 3.0.3 on 2020-12-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0004_auto_20201205_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='code',
            field=models.CharField(max_length=5, null=True),
        ),
    ]