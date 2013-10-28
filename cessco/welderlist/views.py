from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import (CreateView, ListView, DetailView)
from braces.views import LoginRequiredMixin

from .models import Welder
from .models import PerformanceQualification
# from .models import PerformanceQualificationHistory

from forms import WelderCreateForm
from forms import PerformanceQualificationCreateForm
# from forms import WelderPerformanceQualificationFormSet


class WelderListActionMixin(object): 
    @property 
    def action(self): 
        msg = "{0} is missing action." 
        msg = msg.format(self.__class__) 
        raise NotImplementedError(msg) 
 
    def form_valid(self, form): 
        msg = "Welder {0}!" 
        msg = msg.format(self.action) 
        messages.info(self.request, msg) 
        return super(WelderListActionMixin, self).form_valid(form) 

class WelderListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = 'welder_list.html'
    model = Welder
    paginate_by = 20

class WelderDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = 'welder_detail.html'
    model = Welder 
    # form_class = WelderPerformanceQualificationForm
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(WelderDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the performnace qualifications
        context['performance_qualification_list'] = PerformanceQualification.objects.all()
        return context

class WelderCreateView(LoginRequiredMixin, WelderListActionMixin, CreateView):
    login_url = "/login/"
    model = Welder
    template_name = 'welder_form.html'
    form_class = WelderCreateForm
    action = "created"

class PerformanceQualificationCreateView(LoginRequiredMixin, WelderListActionMixin, CreateView):
    login_url = "/login/"
    model = PerformanceQualification
    template_name = 'performancequalification_form.html'
    form_class = PerformanceQualificationCreateForm
    action = "created"

class PerformanceQualificationDetailView(LoginRequiredMixin, DetailView):
    login_url = "/login/"
    template_name = 'performancequalification_detail.html'
    model = PerformanceQualification
    
