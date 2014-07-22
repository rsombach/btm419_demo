# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Unit.comment'
        db.add_column(u'calibration_unit', 'comment',
                      self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Unit.comment'
        db.delete_column(u'calibration_unit', 'comment')


    models = {
        u'calibration.unit': {
            'Meta': {'object_name': 'Unit'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'business_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.BusinessUnitLov']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'renewal_period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UnitRenewalPeriodLov']"}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'unit_make': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UnitMakeLov']"}),
            'unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UnitTypeLov']"})
        },
        u'calibration.unithistory': {
            'Meta': {'object_name': 'UnitHistory'},
            'calibrated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'calibrated_by': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'certificate_issued': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'service_date_time': ('django.db.models.fields.DateField', [], {}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calibration.Unit']"})
        },
        u'core.businessunitlov': {
            'Meta': {'object_name': 'BusinessUnitLov'},
            'business_unit_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'business_unit_description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
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
        }
    }

    complete_apps = ['calibration']