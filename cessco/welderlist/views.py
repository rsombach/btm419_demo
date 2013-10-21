from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from django.views.generic import (ListView, CreateView)
from braces.views import LoginRequiredMixin

from .models import Welder

from forms import WelderCreateForm
 
# def index(request):
#     login_url = "/login/"
#     return render(request, 'welder_form.html',
#     	{ 'welder_add_form' : WelderCreateForm() } )


# Django pattern views
class WelderListView(LoginRequiredMixin, ListView):
	login_url = "/login/"
	model = Welder

class WelderCreateView(LoginRequiredMixin, CreateView):
	login_url = "/login/"
	model = Welder

# template view
# def index(request):
# 	welder_list = Welder.objects.all()
# 	return render(request, 'welderlist/welderlist_base.html',
# 		{'welder_list' : welder_list})
