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
            name='PerformanceQualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('absa_number', models.CharField(max_length=16, verbose_name=b'ABSA Number')),
                ('start_date', models.DateField(null=True, verbose_name=b'Original Test Date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('active', models.BooleanField()),
                ('cessco_weld_procedure', models.ForeignKey(verbose_name=b'Cessco Weld Procedure', to='core.CesscoWeldProcedureLov')),
                ('f_number', models.ForeignKey(verbose_name=b' f Number', to='core.fNumberLov')),
                ('minimum_diameter', models.ForeignKey(verbose_name=b'Minimum Diameter', to='core.DiameterLov')),
                ('position', models.ForeignKey(verbose_name=b'Position', to='core.PositionLov')),
                ('process', models.ForeignKey(verbose_name=b'Process', to='core.ProcessLov')),
                ('t_qual', models.ForeignKey(verbose_name=b' t Qual', to='core.tQualLov')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Welder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('first_name', models.CharField(max_length=128, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=128, verbose_name=b'Last Name')),
                ('welder_stamp', models.ForeignKey(verbose_name=b'Welder Stamp', to='core.WelderStampLov')),
            ],
            options={
                'permissions': (('select_welderlist', 'Can select welder'),),
            },
        ),
        migrations.CreateModel(
            name='WelderHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('start_date', models.DateField(null=True, verbose_name=b'Start Date', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('welder', models.ForeignKey(to='welderlist.Welder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='performancequalification',
            name='welder',
            field=models.ForeignKey(to='welderlist.Welder'),
        ),
    ]
