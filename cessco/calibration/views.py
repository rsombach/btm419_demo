from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from datetime import datetime, timedelta

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import (CreateView, ListView, DetailView, UpdateView, TemplateView)
from django_tables2 import SingleTableView
# import django_tables2 as tables

from braces.views import LoginRequiredMixin

from .models import Unit, UnitHistory

from tables import UnitTable

# forms.py import
from forms import UnitCreateForm
from forms import UnitUpdateForm
from forms import UnitHistoryCreateForm
from forms import UnitHistoryUpdateForm


class CalibrationListActionMixin(object): 
    @property 
    def action(self): 
        msg = "{0} is missing action" 
        msg = msg.format(self.__class__) 
        raise NotImplementedError(msg) 
 
    def form_valid(self, form): 
        msg = "Record {0}" 
        msg = msg.format(self.action) 
        messages.info(self.request, msg) 
        return super(CalibrationListActionMixin, self).form_valid(form)

class UnitListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'unit_list.html'
    model = Unit
    context_object_name = 'unit_list'
    table_class = UnitTable
    table_data = 'unit_list'
    table_pagination = {'per_page': 200}

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitListView, self).get_context_data(**kwargs)

        # Create an object to store query results
        sorted_active_unit_list = []
        unsorted_active_unit_list = []
        unsorted_active_unit_list = Unit.objects.filter(active=True).values('id', 'unit_type__unit_type_code', 'unit_make__unit_make_code', 'model', 'serial_number', 'start_date', 'renewal_period', 'active')#.order_by('unit_type__unit_type_code')
        
        unsorted_active_unit_list_calibration_due_date = []
        unsorted_active_unit_list_calibration_due_date = Unit.objects.filter(active=True)#.order_by('unit_type__unit_type_code')

        # print type(unsorted_active_unit_list)
        # print type(unsorted_active_unit_list_calibration_due_date)

        index = 0

        for row in unsorted_active_unit_list:
            # print "                     unsorted active_unit_list.id = %d" % row['id']
            # print "unsorted_active_unit_list_calibration_due_date.id = %d" % unsorted_active_unit_list_calibration_due_date[index].id

            # update some variable we want to use in the template
            row['calibration_due_date'] = unsorted_active_unit_list_calibration_due_date[index].calibration_due_date
            index = index + 1

        # active_unit_list = sorted(unsorted_active_unit_list, key=lambda k: k['unit_type__unit_type_code'])
        # sorted_active_unit_list = unsorted_active_unit_list.objects.order_by('unit_type__unit_type_code')
        sorted_active_unit_list = unsorted_active_unit_list

        context['unit_list'] = sorted_active_unit_list
        context['unit_list_count'] = sorted_active_unit_list.count()
        return context


class UnitCreateView(LoginRequiredMixin, CalibrationListActionMixin, CreateView):
    login_url = "/login/"
    model = Unit
    template_name = 'unit_form.html'
    form_class = UnitCreateForm
    action = "created"

    # def form_valid(self, form):

    #     form.instance.business_unit = "PREP"
    #     return super(UnitCreateView, self).form_valid(form)


class UnitDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = 'unit_detail.html'
    model = Unit
    table_class = UnitTable
    
    # form_class = WelderPerformanceQualificationForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitDetailView, self).get_context_data(**kwargs)

        kwargs_unit_id = kwargs["object"].id
        self.request.session['current_unit'] = kwargs_unit_id

        unithistory_list = []
        unithistory_list = UnitHistory.objects.filter(unit_id=kwargs_unit_id).order_by('-service_date_time')

        context['unit_history_list'] = unithistory_list
        
        return context


class UnitUpdateView(LoginRequiredMixin, CalibrationListActionMixin, UpdateView):
    login_url = "/login/"
    template_name = 'unit_update.html'
    form_class = UnitUpdateForm
    model = Unit
    action = "updated"

    # def get_form_kwargs(self, *args, **kwargs):
    #     return dict ( super(WelderUpdateView, self).get_form_kwargs(*args, **kwargs), **{'current_welder_id':  self.request.session['current_welder']} )


class UnitHistoryCreateView(LoginRequiredMixin, CalibrationListActionMixin, CreateView):
    login_url = "/login/"
    model = UnitHistory
    template_name = 'unithistory_form.html'
    form_class = UnitHistoryCreateForm
    action = "created"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitHistoryCreateView, self).get_context_data(**kwargs)

        session_unit_id = self.request.session['current_unit']
        current_unit = Unit.objects.get(id=session_unit_id)

        context['current_unit'] = current_unit      
        return context

    def form_valid(self, form):
        form.instance.unit_id = self.request.session['current_unit']

        return super(UnitHistoryCreateView, self).form_valid(form)


class UnitHistoryDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = 'unithistory_detail.html'
    model = UnitHistory
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitHistoryDetailView, self).get_context_data(**kwargs)

        session_unit_id = self.request.session['current_unit']
        current_unit = Unit.objects.get(id=session_unit_id)

        context['current_unit'] = current_unit
        
        return context


class UnitHistoryListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'unithistory_list.html'
    model = UnitHistory
    context_object_name = 'unithistory_list'
    # table_class = UnitHistoryTable
    # table_data = 'unithistory_list'
    # table_pagination = {'per_page': 200}

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitHistoryListView, self).get_context_data(**kwargs)

        session_unit_id = self.request.session['current_unit']
        current_unit = Unit.objects.get(id=session_unit_id)

        current_unithistory_list = []
        current_unithistory_list = UnitHistory.objects.filter(unit_id=session_unit_id).order_by('-service_date_time')

        context['unithistory_list'] = current_unithistory_list
        context['unithistory_list_count'] = len(current_unithistory_list)
        context['current_unit'] = current_unit

        return context

class UnitHistoryUpdateView(LoginRequiredMixin, CalibrationListActionMixin, UpdateView):
    login_url = "/login/"
    template_name = 'unithistory_update.html'
    form_class = UnitHistoryUpdateForm
    model = UnitHistory
    action = "updated"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UnitHistoryUpdateView, self).get_context_data(**kwargs)

        session_unit_id = self.request.session['current_unit']
        current_unit = Unit.objects.get(id=session_unit_id)

        context['current_unit'] = current_unit
        
        return context
