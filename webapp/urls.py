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
    url(r'^$', views.index, name='index'),
    url('^', include('django.contrib.auth.urls')),
]
