import django_tables2 as tables
from .models import Welder
from .models import PerformanceQualification


# django_tables2 definitions

class WelderTable(tables.Table):
    id = tables.LinkColumn('welder_detail', args=[tables.A('pk')])
    absa_number = tables.Column(verbose_name='ABSA Number')
    class Meta:
        model = Welder
        exclude = ( 'created', 'modified', )
        attrs = { "class": "table table-striped table-bordered table-condensed", }

class PerformanceQualificationTable(tables.Table):

    class Meta:
        model = PerformanceQualification
        exclude = ( 'created', 'modified', )
        attrs = { "class": "table table-striped table-bordered table-condensed", }