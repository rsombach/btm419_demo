# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WelderHistory'
        db.create_table(u'welderlist_welderhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('welder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['welderlist.Welder'])),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'welderlist', ['WelderHistory'])


    def backwards(self, orm):
        # Deleting model 'WelderHistory'
        db.delete_table(u'welderlist_welderhistory')


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
        },
        u'welderlist.performancequalification': {
            'Meta': {'object_name': 'PerformanceQualification'},
            'absa_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cessco_weld_procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CesscoWeldProcedureLov']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'f_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.fNumberLov']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_diameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DiameterLov']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PositionLov']"}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ProcessLov']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            't_qual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.tQualLov']"}),
            'welder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['welderlist.Welder']"})
        },
        u'welderlist.welder': {
            'Meta': {'object_name': 'Welder'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'welder_stamp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.WelderStampLov']"})
        },
        u'welderlist.welderhistory': {
            'Meta': {'object_name': 'WelderHistory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'welder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['welderlist.Welder']"})
        }
    }

    complete_apps = ['welderlist']