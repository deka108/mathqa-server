"""
# Name:           cms/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Nov 23, 2016
# Last Modified:  Nov 23, 2016
# Modified by:    Phuc Le-Sanh
"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views
from . import views


urlpatterns = [
    url(r'^topics/$', views.TopicList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
