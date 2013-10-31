# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PerformanceQualificationHistory'
        db.delete_table(u'welderlist_performancequalificationhistory')

        # Adding field 'PerformanceQualification.welder'
        db.add_column(u'welderlist_performancequalification', 'welder',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['welderlist.Welder']),
                      keep_default=False)

        # Adding field 'PerformanceQualification.original_test_date'
        db.add_column(u'welderlist_performancequalification', 'original_test_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'PerformanceQualification.renewal_date'
        db.add_column(u'welderlist_performancequalification', 'renewal_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'PerformanceQualification.active'
        db.add_column(u'welderlist_performancequalification', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PerformanceQualificationHistory'
        db.create_table(u'welderlist_performancequalificationhistory', (
            ('original_test_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('welder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['welderlist.Welder'])),
            ('renewal_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performance_qualification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['welderlist.PerformanceQualification'])),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'welderlist', ['PerformanceQualificationHistory'])

        # Deleting field 'PerformanceQualification.welder'
        db.delete_column(u'welderlist_performancequalification', 'welder_id')

        # Deleting field 'PerformanceQualification.original_test_date'
        db.delete_column(u'welderlist_performancequalification', 'original_test_date')

        # Deleting field 'PerformanceQualification.renewal_date'
        db.delete_column(u'welderlist_performancequalification', 'renewal_date')

        # Deleting field 'PerformanceQualification.active'
        db.delete_column(u'welderlist_performancequalification', 'active')


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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cessco_weld_procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CesscoWeldProcedureLov']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.fNumberLov']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_diameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DiameterLov']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'original_test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PositionLov']"}),
            'pq_card_number': ('django.db.models.fields.IntegerField', [], {}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ProcessLov']"}),
            'renewal_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            't_qual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.tQualLov']"}),
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