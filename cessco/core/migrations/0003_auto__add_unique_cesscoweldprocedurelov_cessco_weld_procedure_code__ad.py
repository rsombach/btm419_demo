# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'CesscoWeldProcedureLov', fields ['cessco_weld_procedure_code']
        db.create_unique(u'core_cesscoweldprocedurelov', ['cessco_weld_procedure_code'])

        # Adding unique constraint on 'ProcessLov', fields ['process_code']
        db.create_unique(u'core_processlov', ['process_code'])

        # Adding unique constraint on 'PositionLov', fields ['position_code']
        db.create_unique(u'core_positionlov', ['position_code'])

        # Adding unique constraint on 'tQualLov', fields ['t_qual_code']
        db.create_unique(u'core_tquallov', ['t_qual_code'])

        # Adding unique constraint on 'fNumberLov', fields ['f_number_code']
        db.create_unique(u'core_fnumberlov', ['f_number_code'])

        # Adding unique constraint on 'DiameterLov', fields ['diameter_code']
        db.create_unique(u'core_diameterlov', ['diameter_code'])

        # Adding unique constraint on 'WelderStampLov', fields ['welder_stamp_code']
        db.create_unique(u'core_welderstamplov', ['welder_stamp_code'])


    def backwards(self, orm):
        # Removing unique constraint on 'WelderStampLov', fields ['welder_stamp_code']
        db.delete_unique(u'core_welderstamplov', ['welder_stamp_code'])

        # Removing unique constraint on 'DiameterLov', fields ['diameter_code']
        db.delete_unique(u'core_diameterlov', ['diameter_code'])

        # Removing unique constraint on 'fNumberLov', fields ['f_number_code']
        db.delete_unique(u'core_fnumberlov', ['f_number_code'])

        # Removing unique constraint on 'tQualLov', fields ['t_qual_code']
        db.delete_unique(u'core_tquallov', ['t_qual_code'])

        # Removing unique constraint on 'PositionLov', fields ['position_code']
        db.delete_unique(u'core_positionlov', ['position_code'])

        # Removing unique constraint on 'ProcessLov', fields ['process_code']
        db.delete_unique(u'core_processlov', ['process_code'])

        # Removing unique constraint on 'CesscoWeldProcedureLov', fields ['cessco_weld_procedure_code']
        db.delete_unique(u'core_cesscoweldprocedurelov', ['cessco_weld_procedure_code'])


    models = {
        u'core.cesscoweldprocedurelov': {
            'Meta': {'object_name': 'CesscoWeldProcedureLov'},
            'cessco_weld_procedure_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'cessco_weld_procedure_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.diameterlov': {
            'Meta': {'object_name': 'DiameterLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'diameter_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'diameter_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.fnumberlov': {
            'Meta': {'object_name': 'fNumberLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'f_number_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.positionlov': {
            'Meta': {'object_name': 'PositionLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'position_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.processlov': {
            'Meta': {'object_name': 'ProcessLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'process_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'process_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.tquallov': {
            'Meta': {'object_name': 'tQualLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            't_qual_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            't_qual_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.welderstamplov': {
            'Meta': {'object_name': 'WelderStampLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'welder_stamp_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'welder_stamp_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['core']