from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from datetime import datetime, timedelta

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import (CreateView, ListView, DetailView, UpdateView, TemplateView)
from django_tables2 import SingleTableView
# import django_tables2 as tables

from braces.views import LoginRequiredMixin

from .models import Welder
from .models import WelderHistory
from .models import PerformanceQualification

# forms.py import
from forms import WelderCreateForm
from forms import WelderUpdateForm
from forms import WelderHistoryCreateForm
from forms import WelderHistoryUpdateForm
from forms import PerformanceQualificationCreateForm
from forms import PerformanceQualificationUpdateForm

# tables.py import
# from tables import WelderTable
from tables import PerformanceQualificationTable

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

class WelderListActionMixin(object): 
    @property 
    def action(self): 
        msg = "{0} is missing action" 
        msg = msg.format(self.__class__) 
        raise NotImplementedError(msg) 
 
    def form_valid(self, form): 
        msg = "Record {0}" 
        msg = msg.format(self.action) 
        messages.info(self.request, msg) 
        return super(WelderListActionMixin, self).form_valid(form)


class WelderListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'welder_list.html'
    model = WelderHistory
    context_object_name = 'welder_list'
    # table_class = WelderTable
    # table_data = 'welder_list'
    # table_pagination = {'per_page': 200}

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WelderListView, self).get_context_data(**kwargs)

        # Create an object to store query results
        active_welder_list = []
        active_welder_list = WelderHistory.objects.filter(end_date__isnull=True).values('id', 'welder_id', 'welder__first_name', 'welder__last_name', 'welder__welder_stamp__welder_stamp_code', 'start_date', 'end_date').order_by('welder__welder_stamp__welder_stamp_code')

        context['welder_list'] = active_welder_list
        context['welder_list_count'] = len(active_welder_list)
        return context
	
	
class SearchResultView(LoginRequiredMixin, TemplateView):
	login_url = "/login/"
	template_name = 'search_results.html'

	def get_context_data(self, **kwargs):
		context = super(SearchResultView, self).get_context_data(**kwargs)
		welder_search_result = []
		performance_qualification_search_result = []
	
		for model, fields in WELDER_MODEL_MAP.iteritems():
			welder_search_result += generic_search( self.request, model, fields, QUERY)
			
		for model, fields in PERFORMANCE_QUALIFICATION_MODEL_MAP.iteritems():
			performance_qualification_search_result += generic_search( self.request, model, fields, QUERY)	
		
		context['welder_search_result'] = welder_search_result
		context['performance_qualification_search_result'] = performance_qualification_search_result
		return context

class WelderDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = 'welder_detail.html'
    model = Welder
    table_class = PerformanceQualificationTable
    
    # form_class = WelderPerformanceQualificationForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WelderDetailView, self).get_context_data(**kwargs)
        
        # Add in a QuerySet of all the performance qualifications for the current welder
        kwargs_welder_id = kwargs["object"].id
        
        context['performance_qualification_list'] = PerformanceQualification.objects.filter(welder_id=kwargs_welder_id, active=True).order_by('id')
        context['welder_history_list'] = WelderHistory.objects.values_list('start_date', flat=True).filter(welder_id=kwargs_welder_id).order_by('-start_date')
        
        self.request.session['current_welder'] = kwargs_welder_id
        self.request.session['current_welder_first_name'] = kwargs["object"].first_name
        self.request.session['current_welder_last_name'] = kwargs["object"].last_name

        return context

class WelderCreateView(LoginRequiredMixin, WelderListActionMixin, CreateView):
    login_url = "/login/"
    model = Welder
    template_name = 'welder_form.html'
    form_class = WelderCreateForm
    action = "created"
    
class WelderUpdateView(LoginRequiredMixin, WelderListActionMixin, UpdateView):
    login_url = "/login/"
    template_name = 'welder_update.html'
    form_class = WelderUpdateForm
    model = Welder
    action = "updated"

    def get_form_kwargs(self, *args, **kwargs):
        return dict ( super(WelderUpdateView, self).get_form_kwargs(*args, **kwargs), **{'current_welder_id':  self.request.session['current_welder']} )

class PerformanceQualificationCreateView(LoginRequiredMixin, WelderListActionMixin, CreateView):
    login_url = "/login/"
    model = PerformanceQualification
    template_name = 'performancequalification_form.html'
    form_class = PerformanceQualificationCreateForm
    action = "created"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PerformanceQualificationCreateView, self).get_context_data(**kwargs)
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']
        
        return context
        
    def form_valid(self, form):
        form.instance.welder_id = self.request.session['current_welder']
        return super(PerformanceQualificationCreateView, self).form_valid(form)


class PerformanceQualificationDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = 'performancequalification_detail.html'
    model = PerformanceQualification
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PerformanceQualificationDetailView, self).get_context_data(**kwargs)
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']
        
        return context
    

class PerformanceQualificationUpdateView(LoginRequiredMixin, WelderListActionMixin, UpdateView):
    login_url = "/login/"
    template_name = 'performancequalification_update.html'
    form_class = PerformanceQualificationUpdateForm
    model = PerformanceQualification
    action = "updated"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PerformanceQualificationUpdateView, self).get_context_data(**kwargs)
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']
        
        return context

class PerformanceQualificationListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'performancequalification_list.html'
    model = PerformanceQualification

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PerformanceQualificationListView, self).get_context_data(**kwargs)
        
        # Add in a QuerySet of all the performance qualifications for the current welder
        session_welder_id = self.request.session['current_welder']
        
        context['performance_qualification_list'] = PerformanceQualification.objects.filter(welder_id=session_welder_id).order_by('id')
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']

        return context
        
class WelderHistoryCreateView(LoginRequiredMixin, WelderListActionMixin, CreateView):
    login_url = "/login/"
    model = WelderHistory
    template_name = 'welderhistory_form.html'
    form_class = WelderHistoryCreateForm
    action = "created"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WelderHistoryCreateView, self).get_context_data(**kwargs)
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']
        
        return context
    
    def form_valid(self, form):
        form.instance.welder_id = self.request.session['current_welder']
        return super(WelderHistoryCreateView, self).form_valid(form)
        
class WelderHistoryDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = 'welderhistory_detail.html'
    model = WelderHistory
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WelderHistoryDetailView, self).get_context_data(**kwargs)
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']
        
        return context

class WelderHistoryListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'welderhistory_list.html'
    model = WelderHistory

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WelderHistoryListView, self).get_context_data(**kwargs)
        
        # Add in a QuerySet of all the history records for the current welder
        session_welder_id = self.request.session['current_welder']
        
        # print "***** welder_id = %d" % session_welder_id
        
        context['welder_history_list'] = WelderHistory.objects.filter(welder_id=session_welder_id).order_by('-start_date')
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']
        
        return context
        
class WelderHistoryUpdateView(LoginRequiredMixin, WelderListActionMixin, UpdateView):
    login_url = "/login/"
    template_name = 'welderhistory_update.html'
    form_class = WelderHistoryUpdateForm
    model = WelderHistory
    action = "updated"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WelderHistoryUpdateView, self).get_context_data(**kwargs)
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']
        
        return context
     
# Performance Qualification Continuity Report
class PerformanceQualificationContinuityReport(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'performancequalification_continuity_report.html'
    model = PerformanceQualification

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PerformanceQualificationContinuityReport, self).get_context_data(**kwargs)

        
        # Add in a QuerySet of all the performance qualifications for the current welder
        session_welder_id = self.request.session['current_welder']
        current_pq = self.kwargs['pk']

        context['current_pq'] = current_pq

        # calculate pq continutity and store in context
        pq = PerformanceQualification.objects.get(id=current_pq, welder_id=session_welder_id)

        pq_continuity = [pq.start_date]
        # print pq_continuity[0]

        days_in_year=365.2425

        # Get the current date
        today = datetime.now().date()

        # add initial two years to original test date
        pq_date = pq.start_date + timedelta(days=(days_in_year*2))
        pq_continuity.append(pq_date)

        if pq_date < today:
            while (pq_date < today):
                # temp_date = datetime.datetime.strptime(pq_continuity[pq_date_count], "%Y-%m-%d").date()
                pq_date = pq_date + timedelta(days=(days_in_year/2))
                pq_continuity.append(pq_date)

        context['pq_continuity'] = pq_continuity
        context['performance_qualification'] = PerformanceQualification.objects.filter(id=current_pq, welder_id=session_welder_id).values('start_date', 'end_date')
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']

        return context

# PDF Rendering
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import get_list_or_404

import ho.pisa as pisa
import cStringIO as StringIO
import cgi

# def write_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     result = StringIO.StringIO()
#     pdf = pisa.pisaDocument(StringIO.StringIO(
#         html.encode("UTF-8")), result)
#     if not pdf.err:
#         return http.HttpResponse(result.getvalue(), \
#              mimetype='application/pdf')
#     return http.HttpResponse('Gremlin's ate your pdf! %s' % cgi.escape(html))
    
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('There were errors when generating the report:<pre>%s</pre>' % escape(html))
    
def WelderReport(request):
    welder_list = get_list_or_404(Welder.objects.order_by('last_name'))
    performance_qualification_list = get_list_or_404(PerformanceQualification.objects.filter(active=True))

    return render_to_pdf( 'welder_report.html', 
    {
        'pagesize' : 'A4',
        'welder_list' : welder_list,
        'performance_qualification_list' : performance_qualification_list,
     } )
