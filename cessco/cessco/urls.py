from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

# from welderlist.views import WelderListView
# from welderlist.views import WelderCreateView

from welderlist import views

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

    # User authentication forms
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

    # Pattern for core app ~ index.html
    url(r'^$', 'core.views.index'),

    # Patterns for Welders
    url(
        regex=r'^welderlist/welder/$',
        view=views.WelderListView.as_view(),
        name='welder_list',
        ),
    url(
        regex=r'^welderlist/welder/add/$',
        view=views.WelderCreateView.as_view(),
        name='welder_add',
        ),
    # url(
    #     regex=r"^welderlist/update/(?P<pk>\d+)/$",
    #     view=views.WelderUpdateView.as_view(),
    #     name="welder_update",
    #     ),
    url(
        regex=r"^welderlist/welder/(?P<pk>\d+)/$",
        view=views.WelderDetailView.as_view(),
        name="welder_detail",
        ),
    # Patterns for Performance Qualifications
    url(
        regex=r'^welderlist/pq/add/$',
        view=views.PerformanceQualificationCreateView.as_view(),
        name='performanequalification_add',
        ),
    url(
        regex=r"^welderlist/pq/(?P<pk>\d+)/$",
        view=views.PerformanceQualificationDetailView.as_view(),
        name="performancequalification_detail",
        ),


)
