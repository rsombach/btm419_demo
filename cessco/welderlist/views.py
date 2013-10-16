# from django.shortcuts import render_to_response
# from django.template import RequestContext

# # Render to html view
# def welderlist(request):
#     return render_to_response('welderlist/index.html')

from django.views.generic.list import ListView
from django.utils import timezone

from welderlist.models import Welder

class WelderListView(ListView):

    model = Welder

    def get_context_data(self, **kwargs):
        context = super(WelderListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
