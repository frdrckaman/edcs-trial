# Generated by Django 3.0 on 2021-01-18 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edc_theme', '0005_auto_20210118_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edcstheme',
            name='user',
        ),
    ]
