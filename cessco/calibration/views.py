from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from datetime import datetime, timedelta

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import (CreateView, ListView, DetailView, UpdateView, TemplateView)
from django_tables2 import SingleTableView

from braces.views import LoginRequiredMixin

from .models import Unit, UnitHistory
from core.models import UnitRenewalPeriodLov

# from tables import UnitTable
from tables import UnitHistoryTable

# forms.py import
from forms import UnitCreateForm
from forms import UnitUpdateForm
from forms import UnitHistoryCreateForm
from forms import UnitHistoryUpdateForm

from .forms import UnitListFormHelper

import re


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
    model = UnitHistory
    template_name = 'unit_list.html'
    context_object_name = 'calibration_unit_list'
    
    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super(UnitListView, self).get_context_data(**kwargs)

            days_in_a_month = (365.2425 / 12)

            # unit_list = []
            unit_list = UnitHistory.objects.filter().values('unit_id', 'unit__unit_type__unit_type_code', 'unit__unit_make__unit_make_code', 'unit__model', 'unit__serial_number', 'service_date_time', 'unit__renewal_period__unit_renewal_period_code').order_by('unit_id', '-service_date_time').distinct('unit_id')

            for unit in unit_list:

                # print unit['service_date_time']
                # print unit['unit__unit_type__unit_type_code']
                # print unit['unit__unit_make__unit_make_code']
                renewal_period = map(int, re.findall('\d+', unit['unit__renewal_period__unit_renewal_period_code']))

                unit['calibration_due_date'] = unit['service_date_time'] + timedelta(days=(renewal_period[0] * days_in_a_month))
                # print unit['calibration_due_date']

            # print unit_list

            context['calibration_unit_list'] = unit_list
            
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
    table_class = UnitHistoryTable
    
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
