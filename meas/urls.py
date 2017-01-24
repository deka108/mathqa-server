"""
# Name:           meas/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Oct 07 2016
# Last Modified:  Nov 23 2016
# Modified by:    Phuc Le-Sanh
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('webapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/', include('cms.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^apiv2/', include('apiv2.urls')),
]
