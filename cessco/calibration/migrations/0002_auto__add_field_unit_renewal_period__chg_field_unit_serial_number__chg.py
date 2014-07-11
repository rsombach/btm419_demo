# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Unit.renewal_period'
        db.add_column(u'calibration_unit', 'renewal_period',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.UnitRenewalPeriodLov']),
                      keep_default=False)


        # Changing field 'Unit.serial_number'
        db.alter_column(u'calibration_unit', 'serial_number', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'Unit.model'
        db.alter_column(u'calibration_unit', 'model', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))
        # Deleting field 'UnitHistory.calibration_date_time'
        db.delete_column(u'calibration_unithistory', 'calibration_date_time')

        # Adding field 'UnitHistory.service_date_time'
        db.add_column(u'calibration_unithistory', 'service_date_time',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 11, 0, 0)),
                      keep_default=False)

        # Adding field 'UnitHistory.calibrated'
        db.add_column(u'calibration_unithistory', 'calibrated',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'UnitHistory.comment'
        db.alter_column(u'calibration_unithistory', 'comment', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True))

    def backwards(self, orm):
        # Deleting field 'Unit.renewal_period'
        db.delete_column(u'calibration_unit', 'renewal_period_id')


        # Changing field 'Unit.serial_number'
        db.alter_column(u'calibration_unit', 'serial_number', self.gf('django.db.models.fields.CharField')(default='default2', max_length=32))

        # Changing field 'Unit.model'
        db.alter_column(u'calibration_unit', 'model', self.gf('django.db.models.fields.CharField')(default='default3', max_length=256))
        # Adding field 'UnitHistory.calibration_date_time'
        db.add_column(u'calibration_unithistory', 'calibration_date_time',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'UnitHistory.service_date_time'
        db.delete_column(u'calibration_unithistory', 'service_date_time')

        # Deleting field 'UnitHistory.calibrated'
        db.delete_column(u'calibration_unithistory', 'calibrated')


        # Changing field 'UnitHistory.comment'
        db.alter_column(u'calibration_unithistory', 'comment', self.gf('django.db.models.fields.CharField')(default='default4', max_length=256))

    models = {
        u'calibration.unit': {
            'Meta': {'object_name': 'Unit'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'business_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.BusinessUnitLov']"}),
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