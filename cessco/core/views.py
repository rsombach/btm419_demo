from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from braces.views import LoginRequiredMixin

from django.views.generic import (TemplateView)

from welderlist.models import Welder
from welderlist.models import PerformanceQualification
from calibration.models import Unit, UnitHistory

# search/util.py import
from search.utils import generic_search
from django.shortcuts  import render_to_response, redirect

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

def index(request):
    return render(request, 'core/core_index.html')

