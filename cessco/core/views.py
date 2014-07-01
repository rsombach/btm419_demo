from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

def index(request):
    return render(request, 'core/core_index.html')
