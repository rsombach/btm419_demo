import django_filters
from .models import Unit

class UnitListFilter(django_filters.FilterSet):
    class Meta:
        model = Unit
        fields = ['business_unit', 'unit_type', 'unit_make']