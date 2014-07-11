# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UnitRenewalPeriodLov'
        db.create_table(u'core_unitrenewalperiodlov', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('unit_renewal_period_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('unit_renewal_period_description', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal(u'core', ['UnitRenewalPeriodLov'])


    def backwards(self, orm):
        # Deleting model 'UnitRenewalPeriodLov'
        db.delete_table(u'core_unitrenewalperiodlov')


    models = {
        u'core.businessunitlov': {
            'Meta': {'object_name': 'BusinessUnitLov'},
            'business_unit_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'business_unit_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.cesscoweldprocedurelov': {
            'Meta': {'object_name': 'CesscoWeldProcedureLov'},
            'cessco_weld_procedure_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'cessco_weld_procedure_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.diameterlov': {
            'Meta': {'object_name': 'DiameterLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'diameter_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'diameter_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.fnumberlov': {
            'Meta': {'object_name': 'fNumberLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'f_number_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.positionlov': {
            'Meta': {'object_name': 'PositionLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'position_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.processlov': {
            'Meta': {'object_name': 'ProcessLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'process_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'process_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.tquallov': {
            'Meta': {'object_name': 'tQualLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            't_qual_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            't_qual_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.unitmakelov': {
            'Meta': {'object_name': 'UnitMakeLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'unit_make_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'unit_make_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.unitrenewalperiodlov': {
            'Meta': {'object_name': 'UnitRenewalPeriodLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'unit_renewal_period_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'unit_renewal_period_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.unittypelov': {
            'Meta': {'object_name': 'UnitTypeLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'unit_type_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'unit_type_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.welderstamplov': {
            'Meta': {'object_name': 'WelderStampLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'welder_stamp_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'welder_stamp_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['core']