from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^$', views.dashboard_index, name='dashboard_index'),
    url(r'^edit/$', views.edit, name='edit'),
]
