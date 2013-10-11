# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'fNumberLov'
        db.create_table(u'core_fnumberlov', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('f_number_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('f_number_description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'core', ['fNumberLov'])

        # Adding model 'ProcessLov'
        db.create_table(u'core_processlov', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('process_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('process_description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'core', ['ProcessLov'])

        # Adding model 'tQualLov'
        db.create_table(u'core_tquallov', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('t_qual_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('t_qual_description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'core', ['tQualLov'])

        # Adding model 'DiameterLov'
        db.create_table(u'core_diameterlov', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('diameter_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('diameter_description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'core', ['DiameterLov'])

        # Adding model 'PositionLov'
        db.create_table(u'core_positionlov', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('position_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('position_description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'core', ['PositionLov'])

        # Adding model 'CesscoWeldProcedureLov'
        db.create_table(u'core_cesscoweldprocedurelov', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('cessco_weld_procedure_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('cessco_weld_procedure_description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'core', ['CesscoWeldProcedureLov'])


    def backwards(self, orm):
        # Deleting model 'fNumberLov'
        db.delete_table(u'core_fnumberlov')

        # Deleting model 'ProcessLov'
        db.delete_table(u'core_processlov')

        # Deleting model 'tQualLov'
        db.delete_table(u'core_tquallov')

        # Deleting model 'DiameterLov'
        db.delete_table(u'core_diameterlov')

        # Deleting model 'PositionLov'
        db.delete_table(u'core_positionlov')

        # Deleting model 'CesscoWeldProcedureLov'
        db.delete_table(u'core_cesscoweldprocedurelov')


    models = {
        u'core.cesscoweldprocedurelov': {
            'Meta': {'object_name': 'CesscoWeldProcedureLov'},
            'cessco_weld_procedure_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'cessco_weld_procedure_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.diameterlov': {
            'Meta': {'object_name': 'DiameterLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'diameter_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'diameter_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.fnumberlov': {
            'Meta': {'object_name': 'fNumberLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'f_number_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.positionlov': {
            'Meta': {'object_name': 'PositionLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'position_description': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'core.processlov': {
            'Meta': {'object_name': 'ProcessLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'process_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'process_description': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'core.tquallov': {
            'Meta': {'object_name': 'tQualLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            't_qual_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            't_qual_description': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['core']