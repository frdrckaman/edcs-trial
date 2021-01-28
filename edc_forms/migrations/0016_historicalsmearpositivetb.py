# Generated by Django 3.0 on 2021-01-28 03:39

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edc_forms', '0015_auto_20210127_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSmearPositiveTB',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('age_15_24', models.IntegerField(verbose_name='15-24')),
                ('age_25_34', models.IntegerField(verbose_name='25-34')),
                ('age_35_44', models.IntegerField(verbose_name='35-44')),
                ('age_45_54', models.IntegerField(verbose_name='45-54')),
                ('age_55_64', models.IntegerField(verbose_name='55-64')),
                ('age_65_above', models.IntegerField(verbose_name='65 and Above')),
                ('gender_male', models.IntegerField(default=0, verbose_name='Male')),
                ('gender_female', models.IntegerField(default=0, verbose_name='Female')),
                ('soc_econ_pos_low', models.IntegerField(default=0, verbose_name='Low')),
                ('soc_econ_pos_middle', models.IntegerField(default=0, verbose_name='Middle')),
                ('soc_econ_pos_high', models.IntegerField(default=0, verbose_name='High')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='edc_forms.RetroYears')),
            ],
            options={
                'verbose_name': 'historical Smear Positive Pulmonary TB',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]