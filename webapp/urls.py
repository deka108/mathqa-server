"""
# Name:           app/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Oct 10 2016
# Last Modified:  Oct 10 2016
# Modified by:    Phuc Le-Sanh
"""

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^$', views.dashboard_index, name='dashboard_index'),

    url(r'^topic/$', views.topic_index, name='topic_index'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$',
        views.topic_detail, name='topic_detail'),
    url(r'^topic/(?P<topic_id>[0-9]+)/concept/(?P<concept_id>[0-9]+)/$',
        views.topic_concept, name='topic_concept'),

    url(r'^adaptive_test/$', views.adaptive_index, name='adaptive_index'),
    url(r'^contest/$', views.contest_index, name='contest_index'),
]
