# Generated by Django 3.0 on 2020-12-30 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_forms', '0006_auto_20201230_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smearpositivetb',
            name='year',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='edc_forms.RetroYears'),
        ),
    ]
