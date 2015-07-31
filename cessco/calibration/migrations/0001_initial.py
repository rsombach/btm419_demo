# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('model', models.CharField(max_length=256, null=True, blank=True)),
                ('serial_number', models.CharField(max_length=32, null=True, verbose_name=b'Serial Number', blank=True)),
                ('start_date', models.DateField(null=True, verbose_name=b'Inservice Date', blank=True)),
                ('active', models.BooleanField()),
                ('comment', models.CharField(max_length=2048, null=True, verbose_name=b'Notes', blank=True)),
                ('business_unit', models.ForeignKey(verbose_name=b'Business Unit', to='core.BusinessUnitLov')),
                ('renewal_period', models.ForeignKey(verbose_name=b'Renewal Period', to='core.UnitRenewalPeriodLov')),
                ('unit_make', models.ForeignKey(verbose_name=b'Unit Make', to='core.UnitMakeLov')),
                ('unit_type', models.ForeignKey(verbose_name=b'Unit Type', to='core.UnitTypeLov')),
            ],
            options={
                'permissions': (('select_calibration', 'Can select unit'),),
            },
        ),
        migrations.CreateModel(
            name='UnitHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('calibrated_by', models.CharField(max_length=256, verbose_name=b'Serviced By')),
                ('comment', models.CharField(max_length=2048, null=True, blank=True)),
                ('certificate_issued', models.BooleanField(verbose_name=b'Certificate Issued')),
                ('service_date_time', models.DateField(verbose_name=b'Service Date')),
                ('calibrated', models.BooleanField(verbose_name=b'Calibrated')),
                ('unit', models.ForeignKey(verbose_name=b'Unit', to='calibration.Unit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
