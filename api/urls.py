"""
# Name:           cms/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Nov 23, 2016
# Last Modified:  Nov 23, 2016
# Modified by:    Phuc Le-Sanh
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^topic_index/$', views.topic_index, name='topic_index'),
    url(r'^topic_post/$', views.topic_post, name='topic_post'),
    url(r'^check_answer/$', views.check_answer, name='check_answer'),
]
