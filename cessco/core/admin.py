from django.contrib import admin
from core.models import fNumberLov
from core.models import ProcessLov
from core.models import tQualLov
from core.models import DiameterLov
from core.models import PositionLov
from core.models import CesscoWeldProcedureLov

admin.site.register(fNumberLov)
admin.site.register(ProcessLov)
admin.site.register(tQualLov)
admin.site.register(DiameterLov)
admin.site.register(PositionLov)
admin.site.register(CesscoWeldProcedureLov)