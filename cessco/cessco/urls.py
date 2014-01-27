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

	# Patterns for Simple search

    url(
        regex=r'^search/$',
        view=views.SearchResultView.as_view(),
        name='searchresult',
        ),
		
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
    url(
        regex=r"^welderlist/welder/update/(?P<pk>\d+)/$",
        view=views.WelderUpdateView.as_view(),
        name="welder_update",
        ),
    url(
        regex=r'^welderlist/welder/(?P<pk>\d+)/$',
        view=views.WelderDetailView.as_view(),
        name='welder_detail',
        ),
        
    # PDF Welder Report
    url(
        regex=r'^welderlist/report/$',
        view=views.WelderReport,
        name='welder_report',
        ),
        
    # Patterns for Performance Qualifications
    url(
        regex=r'^welderlist/pq/$',
        view=views.PerformanceQualificationListView.as_view(),
        name='performancequalification_list',
        ),
    url(
        regex=r'^welderlist/pq/add/$',
        view=views.PerformanceQualificationCreateView.as_view(),
        name='performanequalification_add',
        ),
    url(
        regex=r'^welderlist/pq/(?P<pk>\d+)/$',
        view=views.PerformanceQualificationDetailView.as_view(),
        name='performancequalification_detail',
        ),
    url(
        regex=r'^welderlist/pq/update/(?P<pk>\d+)/$',
        view=views.PerformanceQualificationUpdateView.as_view(),
        name='performanequalification_update',
        ),

    # Performance Qualification Continutity Report
    url(
        regex=r'^welderlist/pq/continuity/(?P<pk>\d+)/$',
        view=views.PerformanceQualificationContinuityReport.as_view(),
        name='performanequalification_update_continutity_report',
        ),
        
    # Patterns for Welder History
    url(
        regex=r'^welderlist/history/add/$',
        view=views.WelderHistoryCreateView.as_view(),
        name='welderhistory_add',
        ),
    url(
        regex=r'^welderlist/history/(?P<pk>\d+)/$',
        view=views.WelderHistoryDetailView.as_view(),
        name='welderhistory_detail',
        ),
    url(
        regex=r'^welderlist/history/$',
        view=views.WelderHistoryListView.as_view(),
        name='welderhistory_list',
        ),
    url(
        regex=r'^welderlist/history/update/(?P<pk>\d+)/$',
        view=views.WelderHistoryUpdateView.as_view(),
        name='welderhistory_update',
        ),

)
