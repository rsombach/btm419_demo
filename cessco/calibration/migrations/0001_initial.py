# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unit'
        db.create_table(u'calibration_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('business_unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.BusinessUnitLov'])),
            ('unit_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UnitTypeLov'])),
            ('unit_make', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'calibration', ['Unit'])

        # Adding model 'UnitHistory'
        db.create_table(u'calibration_unithistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calibration.Unit'])),
            ('calibrated_by', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('certificate_issued', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('calibration_date_time', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'calibration', ['UnitHistory'])


    def backwards(self, orm):
        # Deleting model 'Unit'
        db.delete_table(u'calibration_unit')

        # Deleting model 'UnitHistory'
        db.delete_table(u'calibration_unithistory')


    models = {
        u'calibration.unit': {
            'Meta': {'object_name': 'Unit'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'business_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.BusinessUnitLov']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'unit_make': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UnitTypeLov']"})
        },
        u'calibration.unithistory': {
            'Meta': {'object_name': 'UnitHistory'},
            'calibrated_by': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'calibration_date_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'certificate_issued': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calibration.Unit']"})
        },
        u'core.businessunitlov': {
            'Meta': {'object_name': 'BusinessUnitLov'},
            'business_unit_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'business_unit_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.unittypelov': {
            'Meta': {'object_name': 'UnitTypeLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'unit_type_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'unit_type_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['calibration']