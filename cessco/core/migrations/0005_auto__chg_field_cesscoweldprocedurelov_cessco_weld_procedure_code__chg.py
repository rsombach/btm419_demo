# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CesscoWeldProcedureLov.cessco_weld_procedure_code'
        db.alter_column(u'core_cesscoweldprocedurelov', 'cessco_weld_procedure_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'ProcessLov.process_code'
        db.alter_column(u'core_processlov', 'process_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'PositionLov.position_code'
        db.alter_column(u'core_positionlov', 'position_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'tQualLov.t_qual_code'
        db.alter_column(u'core_tquallov', 't_qual_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'UnitTypeLov.unit_type_code'
        db.alter_column(u'core_unittypelov', 'unit_type_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'UnitMakeLov.unit_make_code'
        db.alter_column(u'core_unitmakelov', 'unit_make_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'fNumberLov.f_number_code'
        db.alter_column(u'core_fnumberlov', 'f_number_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'BusinessUnitLov.business_unit_code'
        db.alter_column(u'core_businessunitlov', 'business_unit_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'DiameterLov.diameter_code'
        db.alter_column(u'core_diameterlov', 'diameter_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

        # Changing field 'WelderStampLov.welder_stamp_code'
        db.alter_column(u'core_welderstamplov', 'welder_stamp_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32))

    def backwards(self, orm):

        # Changing field 'CesscoWeldProcedureLov.cessco_weld_procedure_code'
        db.alter_column(u'core_cesscoweldprocedurelov', 'cessco_weld_procedure_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'ProcessLov.process_code'
        db.alter_column(u'core_processlov', 'process_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'PositionLov.position_code'
        db.alter_column(u'core_positionlov', 'position_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'tQualLov.t_qual_code'
        db.alter_column(u'core_tquallov', 't_qual_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'UnitTypeLov.unit_type_code'
        db.alter_column(u'core_unittypelov', 'unit_type_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'UnitMakeLov.unit_make_code'
        db.alter_column(u'core_unitmakelov', 'unit_make_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'fNumberLov.f_number_code'
        db.alter_column(u'core_fnumberlov', 'f_number_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'BusinessUnitLov.business_unit_code'
        db.alter_column(u'core_businessunitlov', 'business_unit_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'DiameterLov.diameter_code'
        db.alter_column(u'core_diameterlov', 'diameter_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

        # Changing field 'WelderStampLov.welder_stamp_code'
        db.alter_column(u'core_welderstamplov', 'welder_stamp_code', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True))

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