# Generated by Django 3.0 on 2021-01-27 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edc_forms', '0014_auto_20210118_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bacteriologicalconfirmedpulmonarytb',
            name='user',
        ),
        migrations.RemoveField(
            model_name='clusterprevalencesurvey',
            name='user',
        ),
        migrations.RemoveField(
            model_name='retroyears',
            name='user',
        ),
        migrations.RemoveField(
            model_name='smearpositivetb',
            name='user',
        ),
    ]
