from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from datetime import datetime, timedelta

from braces.views import LoginRequiredMixin

from django.views.generic import (TemplateView, ListView)
from django_tables2 import SingleTableView

from welderlist.models import Welder
from welderlist.models import PerformanceQualification
from calibration.models import Unit, UnitHistory

# search/util.py import
from search.utils import generic_search
from django.shortcuts  import render_to_response, redirect

import re


QUERY="q"
WELDER_MODEL_MAP = { 	
				Welder: [ "first_name", "last_name", "welder_stamp__welder_stamp_code" ],
			}
			
PERFORMANCE_QUALIFICATION_MODEL_MAP = {
				PerformanceQualification  : [ "id", "f_number__f_number_code", "process__process_code", "cessco_weld_procedure__cessco_weld_procedure_code" ], 
}

UNIT_MODEL_MAP = {    
	            Unit:  [ "business_unit__business_unit_code", "unit_type__unit_type_code", "unit_make__unit_make_code", "model", "serial_number" ],
            }

class SearchResultView(LoginRequiredMixin, TemplateView):
	login_url = "/login/"
	template_name = 'search_results.html'

	def get_context_data(self, **kwargs):
		context = super(SearchResultView, self).get_context_data(**kwargs)
		welder_search_result = []
		performance_qualification_search_result = []
		unit_search_result = []

		for model, fields in WELDER_MODEL_MAP.iteritems():
			welder_search_result += generic_search( self.request, model, fields, QUERY)

		for model, fields in PERFORMANCE_QUALIFICATION_MODEL_MAP.iteritems():
			performance_qualification_search_result += generic_search( self.request, model, fields, QUERY)	

		for model, fields in UNIT_MODEL_MAP.iteritems():
			unit_search_result += generic_search( self.request, model, fields, QUERY)


		context['welder_search_result'] = welder_search_result
		context['performance_qualification_search_result'] = performance_qualification_search_result
		context['unit_search_result'] = unit_search_result

		search_result_count = len(welder_search_result)
		search_result_count = search_result_count + len(performance_qualification_search_result)
		search_result_count = search_result_count + len(unit_search_result)

		print "search_result_count = %d" % search_result_count

		context['search_result_count'] = len(welder_search_result) + len(performance_qualification_search_result) + len(unit_search_result)

		return context

class CoreDashboardListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'coredashboard_list.html'
    model = UnitHistory
    context_object_name = 'dashboard_calibration_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CoreDashboardListView, self).get_context_data(**kwargs)

        dashboard_calibration_list = []
        days_in_a_month = (365.2425 / 12)
        start_date = datetime.today()

        calibration_list = UnitHistory.objects.filter().values('unit_id', 'unit__unit_type__unit_type_code', 'unit__unit_make__unit_make_code', 'unit__model', 'unit__serial_number', 'service_date_time', 'unit__renewal_period__unit_renewal_period_code').order_by('unit_id', '-service_date_time').distinct('unit_id')

        for calibration in calibration_list:

        	renewal_period = map(int, re.findall('\d+', calibration['unit__renewal_period__unit_renewal_period_code']))

        	calibration['calibration_due_date'] = calibration['service_date_time'] + timedelta(days=(renewal_period[0] * days_in_a_month))

        	end_date = start_date + timedelta(days=7)

        	if start_date.date() <= calibration['calibration_due_date'] <= end_date.date():
        		dashboard_calibration_list.append( [ calibration['unit_id'], calibration['unit__unit_type__unit_type_code'], calibration['unit__unit_make__unit_make_code'], calibration['unit__model'], calibration['unit__serial_number'], calibration['service_date_time'], calibration['calibration_due_date'] ] )

        context['dashboard_calibration_list'] = dashboard_calibration_list
        context['dashboard_calibration_list_count'] = len(dashboard_calibration_list)

        return context


