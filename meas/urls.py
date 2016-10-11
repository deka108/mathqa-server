"""
# Name:           meas/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Oct 07 2016
# Last Modified:  Oct 10 2016
# Modified by:    Phuc Le-Sanh
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webapp/', include('webapp.urls')),
]
