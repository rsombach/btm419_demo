from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import (CreateView, ListView, DetailView, UpdateView)
from django_tables2 import SingleTableView
# import django_tables2 as tables

from braces.views import LoginRequiredMixin

from .models import Welder
from .models import PerformanceQualification

# forms.py import
from forms import WelderCreateForm
from forms import WelderUpdateForm
from forms import PerformanceQualificationCreateForm
from forms import PerformanceQualificationUpdateForm

# tables.py import
from tables import WelderTable, PerformanceQualificationTable


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


class WelderListView(SingleTableView, LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'welder_list.html'
    model = Welder
    context_object_name = 'welder_list'
    table_class = WelderTable
    table_pagination = {'per_page': 25}


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
        
        context['performance_qualification_list'] = PerformanceQualification.objects.filter(welder_id=kwargs_welder_id, active=True)

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
        
        context['performance_qualification_list'] = PerformanceQualification.objects.filter(welder_id=session_welder_id)
        context['current_welder'] = self.request.session['current_welder']
        context['current_welder_first_name'] = self.request.session['current_welder_first_name']
        context['current_welder_last_name'] = self.request.session['current_welder_last_name']

        return context
