# Generated by Django 3.0 on 2021-01-06 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_forms', '0010_auto_20210106_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smearpositivetb',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_forms.RetroYears'),
        ),
    ]