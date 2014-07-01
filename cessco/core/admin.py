from django.contrib import admin

# Core
from core.models import BusinessUnitLov

# Welderlist
from core.models import fNumberLov
from core.models import ProcessLov
from core.models import tQualLov
from core.models import DiameterLov
from core.models import PositionLov
from core.models import CesscoWeldProcedureLov
from core.models import WelderStampLov

# Calibration
from core.models import UnitTypeLov
from core.models import UnitMakeLov


# Globally disable delete selected on list views
admin.site.disable_action('delete_selected')

# Core admin
class BusinessUnitLovAdmin(admin.ModelAdmin):
	list_display = ['business_unit_code', 'business_unit_description']
	
	def has_delete_permission(self, request, obj=None):
	        return_value = False


# Welderlist admin
class fNumberLovAdmin(admin.ModelAdmin):
	list_display = ['f_number_code', 'f_number_description']
	
	def has_delete_permission(self, request, obj=None):
	        return_value = False
	

class ProcessLovAdmin(admin.ModelAdmin):
	list_display = ['process_code', 'process_description']
	
	def has_delete_permission(self, request, obj=None):
	        return_value = False


class tQualLovAdmin(admin.ModelAdmin):
	list_display = ['t_qual_code', 't_qual_description']

	def has_delete_permission(self, request, obj=None):
	        return_value = False


class DiameterLovAdmin(admin.ModelAdmin):
	list_display = ['diameter_code', 'diameter_description']

	def has_delete_permission(self, request, obj=None):
	        return_value = False


class PositionLovAdmin(admin.ModelAdmin):
	list_display = ['position_code', 'position_description']

	def has_delete_permission(self, request, obj=None):
	        return_value = False


class CesscoWeldProcedureLovAdmin(admin.ModelAdmin):
	list_display = ['cessco_weld_procedure_code', 'cessco_weld_procedure_description']

	def has_delete_permission(self, request, obj=None):
	        return_value = False


class WelderStampLovAdmin(admin.ModelAdmin):
	list_display = ['welder_stamp_code', 'welder_stamp_description']
	
	def has_delete_permission(self, request, obj=None):
	        return_value = False

# Welderlist admin
class UnitTypeLovAdmin(admin.ModelAdmin):
	list_display = ['unit_type_code', 'unit_type_description']
	
	def has_delete_permission(self, request, obj=None):
	        return_value = False

class UnitMakeLovAdmin(admin.ModelAdmin):
	list_display = ['unit_make_code', 'unit_make_description']
	
	def has_delete_permission(self, request, obj=None):
	        return_value = False



admin.site.register(BusinessUnitLov, BusinessUnitLovAdmin)

admin.site.register(fNumberLov, fNumberLovAdmin)
admin.site.register(ProcessLov, ProcessLovAdmin)
admin.site.register(tQualLov, tQualLovAdmin)
admin.site.register(DiameterLov, DiameterLovAdmin)
admin.site.register(PositionLov, PositionLovAdmin)
admin.site.register(CesscoWeldProcedureLov, CesscoWeldProcedureLovAdmin)
admin.site.register(WelderStampLov, WelderStampLovAdmin)

admin.site.register(UnitTypeLov, UnitTypeLovAdmin)
admin.site.register(UnitMakeLov, UnitMakeLovAdmin)
