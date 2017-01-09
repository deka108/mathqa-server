"""
# Name:           webapp/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Oct 10 2016
# Last Modified:  Nov 21 2016
# Modified by:    Phuc Le-Sanh
"""
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^$', views.dashboard_index, name='dashboard_index'),
    url(r'^custom_login/$', views.custom_login, name='custom_login'),

    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^edit_user/$', views.edit_user, name='edit_user'),
    url(r'^api_create_user/$', views.api_create_user,
        name='api_create_user'),
    url(r'^api_update_user/$', views.api_update_user,
        name='api_update_user'),
    url(r'^topic/$', views.topic_index, name='topic_index'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$',
        views.topic_detail, name='topic_detail'),
    url(r'^topic/(?P<topic_id>[0-9]+)/concept/(?P<concept_id>[0-9]+)/$',
        views.topic_concept, name='topic_concept'),

    url(r'^adaptive_test/$', views.adaptive_index, name='adaptive_index'),
    url(r'^search_question?keyword=(?P<keyword>.+)/$',
        views.search_question, name='search_question'),
    url(r'^search_question/$',
        views.search_question, name='search_question'),
]
