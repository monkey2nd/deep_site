# Generated by Django 3.1.4 on 2021-01-09 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deeplarning', '0002_check_photo_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check_photo',
            name='title',
        ),
    ]
