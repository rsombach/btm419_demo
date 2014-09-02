import django_tables2 as tables

from .models import Unit


class UnitTable(tables.Table):
    unit_type = tables.LinkColumn('unit_detail', args=[tables.A('pk')], verbose_name=('Type'))
    unit_make = tables.LinkColumn('unit_detail', args=[tables.A('pk')], verbose_name=('Make'))
    model = tables.LinkColumn('unit_detail', args=[tables.A('pk')], verbose_name=('Model'))
    serial_number = tables.LinkColumn('unit_detail', args=[tables.A('pk')], verbose_name=('Serial Number'))
    calibration_due_date = tables.LinkColumn('unit_detail', args=[tables.A('pk')], verbose_name=('Calibration Due Date'))

    class Meta:
        model = Unit
        fields = ( 'unit_type', 'unit_make', 'model', 'serial_number', 'calibration_due_date', )
        order_by = ('unit_type', )
        attrs = { "class": "table table-striped table-bordered table-condensed", }
