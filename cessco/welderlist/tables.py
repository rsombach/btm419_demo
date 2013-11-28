import django_tables2 as tables
from .models import Welder
from .models import PerformanceQualification


# django_tables2 definitions

class WelderTable(tables.Table):
    welder_stamp = tables.LinkColumn('welder_detail', args=[tables.A('pk')], attrs={"th": {"width": "20%"}})
    first_name = tables.LinkColumn('welder_detail', args=[tables.A('pk')])
    last_name = tables.LinkColumn('welder_detail', args=[tables.A('pk')])

    class Meta:
        model = Welder
        exclude = ( 'id', 'created', 'modified', )
        sequence = ("welder_stamp", "first_name", "last_name")
        attrs = { "class": "table table-striped table-bordered table-condensed", }

class PerformanceQualificationTable(tables.Table):

    class Meta:
        model = PerformanceQualification
        exclude = ( 'created', 'modified', )
        attrs = { "class": "table table-striped table-bordered table-condensed", }