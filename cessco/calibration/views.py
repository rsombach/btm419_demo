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
        active_unit_list = []
        active_unit_list = Unit.objects.filter(active=True).values('id', 'unit_type', 'unit_make', 'model', 'serial_number', 'start_date', 'active')

        context['unit_list'] = active_unit_list
        context['unit_list_count'] = len(active_unit_list)
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
        return context


        