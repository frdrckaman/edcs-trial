# Generated by Django 3.0 on 2020-10-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('edc_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sites',
            field=models.ManyToManyField(blank=True, to='sites.Site'),
        ),
    ]