from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.generic.list import ListView
from django.utils import timezone

from welderlist.models import Welder

# class WelderListView(ListView):

#     model = Welder

#     def get_context_data(self, **kwargs):
#         context = super(WelderListView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context

def index(request):
	welder_list = Welder.objects.all()
	return render(request, 'welderlist/welder_list.html',
		{'welder_list' : welder_list})
