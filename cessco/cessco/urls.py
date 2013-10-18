from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

from welderlist.views import WelderListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cessco.views.home', name='home'),
    # url(r'^cessco/', include('cessco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Pattern for core app
    url(r'^$', 'core.views.index'),

    # Pattern for Welder List
    url(r'^welderlist/$', WelderListView.as_view(), name='welderlist-index'),
)
