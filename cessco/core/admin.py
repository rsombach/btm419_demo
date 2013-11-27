from django.contrib import admin
from core.models import fNumberLov
from core.models import ProcessLov
from core.models import tQualLov
from core.models import DiameterLov
from core.models import PositionLov
from core.models import CesscoWeldProcedureLov
from core.models import WelderStampLov

# Globally disable delete selected on list views
admin.site.disable_action('delete_selected')
	
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


admin.site.register(fNumberLov, fNumberLovAdmin)
admin.site.register(ProcessLov, ProcessLovAdmin)
admin.site.register(tQualLov, tQualLovAdmin)
admin.site.register(DiameterLov, DiameterLovAdmin)
admin.site.register(PositionLov, PositionLovAdmin)
admin.site.register(CesscoWeldProcedureLov, CesscoWeldProcedureLovAdmin)
admin.site.register(WelderStampLov, WelderStampLovAdmin)