from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic import (CreateView, ListView, DetailView)
from braces.views import LoginRequiredMixin

from .models import Welder

from forms import WelderCreateForm


class WelderListActionMixin(object): 
    @property 
    def action(self): 
        # This method optimized for 
        #   ebook display 
        msg = "{0} is missing action." 
        msg = msg.format(self.__class__) 
        raise NotImplementedError(msg) 
 
    def form_valid(self, form): 
        # This method optimized for 
        #   ebook display 
        msg = "Welder {0}!" 
        msg = msg.format(self.action) 
        messages.info(self.request, msg) 
        return super(WelderListActionMixin, self).form_valid(form) 

class WelderListView(LoginRequiredMixin, ListView):
	login_url = "/login/"
	model = Welder
	paginate_by = 20


class WelderDetailView(LoginRequiredMixin, DetailView):
	login_url = "/login/"
	model = Welder



class WelderCreateView(LoginRequiredMixin, WelderListActionMixin, CreateView):
	login_url = "/login/"
	model = Welder
	template_name = '/welderlist/welderlist_create.html'
	form_class = WelderCreateForm
	action = "created"
