from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^topic/$', views.topic_index, name='topic_index'),
    url(r'^edit_topic/(?P<topic_id>[0-9]+)/$',
        views.edit_topic, name='edit_topic'),
    url(r'^create_topic/$',
        views.create_topic, name='create_topic'),
    url(r'^api_update_topic/$', views.api_update_topic,
        name='api_update_topic'),
    url(r'^api_create_topic/$', views.api_create_topic,
        name='api_create_topic'),
]
