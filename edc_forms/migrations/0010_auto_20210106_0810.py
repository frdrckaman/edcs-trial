# Generated by Django 3.0 on 2021-01-06 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edc_forms', '0009_auto_20210106_0808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smearpositivetb',
            old_name='year_id',
            new_name='year',
        ),
    ]
