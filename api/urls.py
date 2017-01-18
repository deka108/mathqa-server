"""
# Name:           cms/urls.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   Nov 23, 2016
# Last Modified:  Nov 23, 2016
# Modified by:    Phuc Le-Sanh
"""
from django.conf.urls import url, include
# from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# router = routers.SimpleRouter()
# router.register("question/search", QuestionSearchView, base_name="question-search")

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^topics/$', views.TopicList.as_view(), name='topic-list'),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view(),
        name='topic-detail'),
    url(r'^concepts/$', views.ConceptList.as_view(), name='concept-list'),
    url(r'^concepts/(?P<pk>[0-9]+)/$', views.ConceptDetail.as_view(),
        name='concept-detail'),
    url(r'^papers/$', views.PaperList.as_view(), name='paper-list'),
    url(r'^papers/(?P<pk>[0-9]+)/$', views.PaperDetail.as_view(),
        name='paper-detail'),
    url(r'^questions/$', views.QuestionList.as_view(), name='question-list'),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(),
        name='question-detail'),
    url(r'^answerparts/$', views.AnswerPartList.as_view(),
        name='answerpart-list'),
    url(r'^answerparts/(?P<pk>[0-9]+)/$', views.AnswerPartDetail.as_view(),
        name='answerpart-detail'),

    # education levels
    url(r'^subjects/$', views.SubjectList.as_view(), name='subject-list'),
    url(r'^subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view(),
        name='subject-detail'),

    # topics
    url(r'^(?P<subj_id>[0-9]+)/topics/$', views.TopicList.as_view(),
        name='subj-topic-list'),

    # Concepts
    url(r'^(?P<subj_id>[0-9]+)/concepts/$', views.ConceptList.as_view(),
        name='subj-concept-list'),
    url(r'^topics/(?P<topic_id>[0-9]+)/concepts/$',
        views.ConceptList.as_view(), name='topic-concept-list'),

    # Questions
    url(r'^(?P<subj_id>[0-9]+)/questions/$', views.QuestionList.as_view(),
        name='subj-question-list'),
    url(r'^topics/(?P<topic_id>[0-9]+)/questions/$',
        views.QuestionList.as_view(), name='topic-question-list'),
    url(r'^concepts/(?P<concept_id>[0-9]+)/questions/$',
        views.QuestionList.as_view(), name='concept-question-list'),

    # Keypoints
    url(r'^keypoints/$', views.KeyPointList.as_view(), name='keypoint-list'),
    url(r'^keypoints/(?P<pk>[0-9]+)/$', views.KeyPointDetail.as_view(),
        name='keypoint-detail'),
    url(r'^concepts/(?P<concept_id>[0-9]+)/keypoints/$',
        views.KeyPointList.as_view(), name='concept-keypoint-list'),

    # Sample Questions
    url(r'^samplequestions/$', views.QuestionList.as_view(),
        name='samplequestion-list'),
    url(r'^concepts/(?P<concept_id>[0-9]+)/samplequestions/$',
        views.QuestionList.as_view(), name='concept-samplequestion-list'),

    # Sample Questions
    url(r'^realquestions/$', views.QuestionList.as_view(),
        name='realquestion-list'),
    url(r'^concepts/(?P<concept_id>[0-9]+)/realquestions/$',
        views.QuestionList.as_view(), name='concept-realquestion-list'),

    # Formulas
    url(r'^formulas/$', views.FormulaList.as_view(), name="formula-list"),
    url(r'^formulas/(?P<pk>[0-9]+)/$', views.FormulaDetail.as_view(),
        name="formula-detail"),
    url(r'^formulas/reindex/all', views.reindex_all_formula,
        name="formula-reindex-all"),

    # FormulaIndex
    url(r'^formulaindexes/$', views.FormulaIndexList.as_view(),
        name="formula-index-list"),

    # Search
    url(r'^search/db$', views.search_text_db, name="search_db_text"),
    url(r'^fsearch/$', views.search_formula, name="search_formula"),

    # url(r'^searchf$', ),

    # account
    # url(r'^register/$', ),
    # url(r'^logout/$', ),
]

urlpatterns += [
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
