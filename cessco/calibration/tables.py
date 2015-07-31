import django_tables2 as tables

from .models import UnitHistory
from core.models import UnitRenewalPeriodLov

class UnitHistoryTable(tables.Table):

    class Meta:
        model = UnitHistory
        exclude = ('created', 'modified', )
        order_by = ('unit_type', )
        attrs = { "class": "table table-striped table-bordered table-condensed", }
