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

    url(r'^concept/$', views.concept_index, name='concept_index'),
    url(r'^concept/(?P<topic_id>[0-9]+)/$',
        views.concept_index, name='concept_index'),
    url(r'^edit_concept/(?P<concept_id>[0-9]+)/$',
        views.edit_concept, name='edit_concept'),
    url(r'^create_concept/$',
        views.create_concept, name='create_concept'),
    url(r'^api_update_concept/$', views.api_update_concept,
        name='api_update_concept'),
    url(r'^api_create_concept/$', views.api_create_concept,
        name='api_create_concept'),
]
