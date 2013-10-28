# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PerformanceQualificationHistory.performance_qualification_id'
        db.delete_column(u'welderlist_performancequalificationhistory', 'performance_qualification_id_id')

        # Deleting field 'PerformanceQualificationHistory.welder_id'
        db.delete_column(u'welderlist_performancequalificationhistory', 'welder_id_id')

        # Adding field 'PerformanceQualificationHistory.welder'
        db.add_column(u'welderlist_performancequalificationhistory', 'welder',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['welderlist.Welder']),
                      keep_default=False)

        # Adding field 'PerformanceQualificationHistory.performance_qualification'
        db.add_column(u'welderlist_performancequalificationhistory', 'performance_qualification',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['welderlist.PerformanceQualification']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PerformanceQualificationHistory.performance_qualification_id'
        db.add_column(u'welderlist_performancequalificationhistory', 'performance_qualification_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['welderlist.PerformanceQualification']),
                      keep_default=False)

        # Adding field 'PerformanceQualificationHistory.welder_id'
        db.add_column(u'welderlist_performancequalificationhistory', 'welder_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['welderlist.Welder']),
                      keep_default=False)

        # Deleting field 'PerformanceQualificationHistory.welder'
        db.delete_column(u'welderlist_performancequalificationhistory', 'welder_id')

        # Deleting field 'PerformanceQualificationHistory.performance_qualification'
        db.delete_column(u'welderlist_performancequalificationhistory', 'performance_qualification_id')


    models = {
        u'core.cesscoweldprocedurelov': {
            'Meta': {'object_name': 'CesscoWeldProcedureLov'},
            'cessco_weld_procedure_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'cessco_weld_procedure_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.diameterlov': {
            'Meta': {'object_name': 'DiameterLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'diameter_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'diameter_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.fnumberlov': {
            'Meta': {'object_name': 'fNumberLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'f_number_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.positionlov': {
            'Meta': {'object_name': 'PositionLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'position_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.processlov': {
            'Meta': {'object_name': 'ProcessLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'process_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'process_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'core.tquallov': {
            'Meta': {'object_name': 'tQualLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            't_qual_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            't_qual_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        },
        u'welderlist.performancequalification': {
            'Meta': {'object_name': 'PerformanceQualification'},
            'cessco_weld_procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CesscoWeldProcedureLov']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.fNumberLov']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_diameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DiameterLov']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PositionLov']"}),
            'pq_card_number': ('django.db.models.fields.IntegerField', [], {}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ProcessLov']"}),
            't_qual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.tQualLov']"})
        },
        u'welderlist.performancequalificationhistory': {
            'Meta': {'object_name': 'PerformanceQualificationHistory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'original_test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'performance_qualification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['welderlist.PerformanceQualification']"}),
            'renewal_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'welder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['welderlist.Welder']"})
        },
        u'welderlist.welder': {
            'Meta': {'object_name': 'Welder'},
            'absa_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'welderlist.welderstamp': {
            'Meta': {'object_name': 'WelderStamp'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'stamp': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['welderlist']