import django_tables2 as tables

from .models import Unit
from .models import UnitHistory


class UnitTable(tables.Table):

    class Meta:
        model = Unit
        exclude = ( 'created', 'modified', )
        attrs = { "class": "table table-striped table-bordered table-condensed", }