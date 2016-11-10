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
    url(r'^topic/move_up/(?P<topic_id>[0-9]+)/$',
        views.move_up, name='move_up'),
    url(r'^topic/move_down/(?P<topic_id>[0-9]+)/$',
        views.move_down, name='move_down'),
    url(r'^delete_topic/(?P<topic_id>[0-9]+)/$',
        views.delete_topic, name='delete_topic'),

    url(r'^concept/$', views.concept_index, name='concept_index'),
    url(r'^concept_subject/$',
        views.concept_subject, name='concept_subject'),

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
    url(r'^delete_concept/(?P<concept_id>[0-9]+)/$',
        views.delete_concept, name='delete_concept'),

    url(r'^question/$', views.question_index, name='question_index'),
    url(r'^create_question/$', views.create_question, name='create_question'),

    url(r'^paper/$', views.paper_index, name='paper_index'),
    url(r'^create_paper/$', views.create_paper, name='create_paper'),
    url(r'^api_create_paper/$', views.api_create_paper,
        name='api_create_paper'),
    url(r'^edit_paper/(?P<paper_id>[0-9]+)/$',
        views.edit_paper, name='edit_paper'),
    url(r'^api_update_paper/$', views.api_update_paper,
        name='api_update_paper'),
    url(r'^delete_paper/(?P<paper_id>[0-9]+)/$',
        views.delete_paper, name='delete_paper'),
]
