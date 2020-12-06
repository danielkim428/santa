# Generated by Django 3.0.3 on 2020-12-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0017_auto_20201206_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='reveal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='letter',
            name='content',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]