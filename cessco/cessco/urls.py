from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

# from welderlist.views import WelderListView
# from welderlist.views import WelderCreateView

from welderlist import views as welderlist_views
from calibration import views as calibration_views

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

    # welderlist
    url(
        regex=r'^search/$',
        view=welderlist_views.SearchResultView.as_view(),
        name='searchresult',
        ),

    # Patterns for Welders
    url(
        regex=r'^welderlist/welder/$',
        view=welderlist_views.WelderListView.as_view(),
        name='welder_list',
        ),
    url(
        regex=r'^welderlist/welder/add/$',
        view=welderlist_views.WelderCreateView.as_view(),
        name='welder_add',
        ),
    url(
        regex=r"^welderlist/welder/update/(?P<pk>\d+)/$",
        view=welderlist_views.WelderUpdateView.as_view(),
        name="welder_update",
        ),
    url(
        regex=r'^welderlist/welder/(?P<pk>\d+)/$',
        view=welderlist_views.WelderDetailView.as_view(),
        name='welder_detail',
        ),
        
    # PDF Welder Report
    url(
        regex=r'^welderlist/report/$',
        view=welderlist_views.WelderReport,
        name='welder_report',
        ),
        
    # Patterns for Performance Qualifications
    url(
        regex=r'^welderlist/pq/$',
        view=welderlist_views.PerformanceQualificationListView.as_view(),
        name='performancequalification_list',
        ),
    url(
        regex=r'^welderlist/pq/add/$',
        view=welderlist_views.PerformanceQualificationCreateView.as_view(),
        name='performanequalification_add',
        ),
    url(
        regex=r'^welderlist/pq/(?P<pk>\d+)/$',
        view=welderlist_views.PerformanceQualificationDetailView.as_view(),
        name='performancequalification_detail',
        ),
    url(
        regex=r'^welderlist/pq/update/(?P<pk>\d+)/$',
        view=welderlist_views.PerformanceQualificationUpdateView.as_view(),
        name='performanequalification_update',
        ),

    # Performance Qualification Continutity Report
    url(
        regex=r'^welderlist/pq/continuity/(?P<pk>\d+)/$',
        view=welderlist_views.PerformanceQualificationContinuityReport.as_view(),
        name='performanequalification_update_continutity_report',
        ),
        
    # Patterns for Welder History
    url(
        regex=r'^welderlist/history/add/$',
        view=welderlist_views.WelderHistoryCreateView.as_view(),
        name='welderhistory_add',
        ),
    url(
        regex=r'^welderlist/history/(?P<pk>\d+)/$',
        view=welderlist_views.WelderHistoryDetailView.as_view(),
        name='welderhistory_detail',
        ),
    url(
        regex=r'^welderlist/history/$',
        view=welderlist_views.WelderHistoryListView.as_view(),
        name='welderhistory_list',
        ),
    url(
        regex=r'^welderlist/history/update/(?P<pk>\d+)/$',
        view=welderlist_views.WelderHistoryUpdateView.as_view(),
        name='welderhistory_update',
        ),

    # Patterns for Calibration app ~ index.html
    # url(r'^calibration/$', 'calibration.views.index'),
    url(
        regex=r'^calibration/unit/$',
        view=calibration_views.UnitListView.as_view(),
        name='unit_list',
        ),
    url(
        regex=r'^calibration/unit/(?P<pk>\d+)/$',
        view=calibration_views.UnitDetailView.as_view(),
        name='unit_detail',
        ),
    url(
        regex=r'^calibration/unit/add/$',
        view=calibration_views.UnitCreateView.as_view(),
        name='unit_add',
        ),
    url(
        regex=r"^calibration/unit/update/(?P<pk>\d+)/$",
        view=calibration_views.UnitUpdateView.as_view(),
        name="unit_update",
        ),
    # Patterns for Calibration Unit History
    url(
        regex=r'^calibration/history/$',
        view=calibration_views.UnitHistoryListView.as_view(),
        name='unithistory_list',
        ),
    url(
        regex=r'^calibration/history/add/$',
        view=calibration_views.UnitHistoryCreateView.as_view(),
        name='unithistory_add',
        ),
    url(
        regex=r'^calibration/history/(?P<pk>\d+)/$',
        view=calibration_views.UnitHistoryDetailView.as_view(),
        name='unithistory_detail',
        ),
    url(
        regex=r"^calibration/history/update/(?P<pk>\d+)/$",
        view=calibration_views.UnitHistoryUpdateView.as_view(),
        name="unithistory_update",
        ),
)
