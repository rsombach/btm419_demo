# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnitLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('business_unit_code', models.CharField(unique=True, max_length=32, verbose_name=b'Business Unit Code')),
                ('business_unit_description', models.CharField(max_length=256, verbose_name=b'Business Unit Description', blank=True)),
            ],
            options={
                'verbose_name': 'Business Unit ',
                'verbose_name_plural': 'Business Unit ',
            },
        ),
        migrations.CreateModel(
            name='CesscoWeldProcedureLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('cessco_weld_procedure_code', models.CharField(unique=True, max_length=32, verbose_name=b'Cessco Weld Procedure Code')),
                ('cessco_weld_procedure_description', models.CharField(max_length=256, verbose_name=b'Cessco Weld Procedure Description', blank=True)),
            ],
            options={
                'verbose_name': 'Cessco Weld Procedure ',
                'verbose_name_plural': 'Cessco Weld Procedure ',
            },
        ),
        migrations.CreateModel(
            name='DiameterLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('diameter_code', models.CharField(unique=True, max_length=32, verbose_name=b'Diameter Code')),
                ('diameter_description', models.CharField(max_length=256, verbose_name=b'Diameter Description', blank=True)),
            ],
            options={
                'verbose_name': 'Diameter ',
                'verbose_name_plural': 'Diameter ',
            },
        ),
        migrations.CreateModel(
            name='fNumberLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('f_number_code', models.CharField(unique=True, max_length=32, verbose_name=b' f Number Code')),
                ('f_number_description', models.CharField(max_length=256, verbose_name=b' f Number Description', blank=True)),
            ],
            options={
                'verbose_name': ' f Number',
                'verbose_name_plural': ' f Number ',
            },
        ),
        migrations.CreateModel(
            name='PositionLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('position_code', models.CharField(unique=True, max_length=32, verbose_name=b'Position Code')),
                ('position_description', models.CharField(max_length=256, verbose_name=b'Position Description', blank=True)),
            ],
            options={
                'verbose_name': 'Position ',
                'verbose_name_plural': 'Position ',
            },
        ),
        migrations.CreateModel(
            name='ProcessLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('process_code', models.CharField(unique=True, max_length=32, verbose_name=b'Process Code')),
                ('process_description', models.CharField(max_length=256, verbose_name=b'Process Description', blank=True)),
            ],
            options={
                'verbose_name': 'Process ',
                'verbose_name_plural': 'Process ',
            },
        ),
        migrations.CreateModel(
            name='tQualLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('t_qual_code', models.CharField(unique=True, max_length=32, verbose_name=b' t Qual Code')),
                ('t_qual_description', models.CharField(max_length=256, verbose_name=b' t Qual Description', blank=True)),
            ],
            options={
                'verbose_name': ' t Qual ',
                'verbose_name_plural': ' t Qual ',
            },
        ),
        migrations.CreateModel(
            name='UnitMakeLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('unit_make_code', models.CharField(unique=True, max_length=32, verbose_name=b'Unit Make Code')),
                ('unit_make_description', models.CharField(max_length=256, verbose_name=b'Unit Make Description', blank=True)),
            ],
            options={
                'verbose_name': 'Unit Make ',
                'verbose_name_plural': 'Unit Make ',
            },
        ),
        migrations.CreateModel(
            name='UnitRenewalPeriodLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('unit_renewal_period_code', models.CharField(unique=True, max_length=32, verbose_name=b'Unit Renewal Period Code')),
                ('unit_renewal_period_description', models.CharField(max_length=256, verbose_name=b'Unit Renewal Period Description', blank=True)),
            ],
            options={
                'verbose_name': 'Unit Renewal Period ',
                'verbose_name_plural': 'Unit Renewal Period ',
            },
        ),
        migrations.CreateModel(
            name='UnitTypeLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('unit_type_code', models.CharField(unique=True, max_length=32, verbose_name=b'Unit Type Code')),
                ('unit_type_description', models.CharField(max_length=256, verbose_name=b'Unit Type Description', blank=True)),
            ],
            options={
                'verbose_name': 'Unit Type ',
                'verbose_name_plural': 'Unit Type ',
            },
        ),
        migrations.CreateModel(
            name='WelderStampLov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('welder_stamp_code', models.CharField(unique=True, max_length=32, verbose_name=b'Welder Stamp Code')),
                ('welder_stamp_description', models.CharField(max_length=256, verbose_name=b'Welder Stamp Description', blank=True)),
            ],
            options={
                'verbose_name': 'Welder Stamp ',
                'verbose_name_plural': 'Welder Stamp ',
            },
        ),
    ]
