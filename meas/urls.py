"""
# Name:           meas/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Oct 07 2016
# Last Modified:  Oct 24 2016
# Modified by:    Phuc Le-Sanh
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('webapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^cms/', include('cms.urls')),
]
