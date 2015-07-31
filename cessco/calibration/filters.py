import django_filters
from .models import UnitHistory

class UnitListFilter(django_filters.FilterSet):
    class Meta:
        model = UnitHistory
        fields = ['unit__business_unit', 'unit__unit_type', 'unit__unit_make']