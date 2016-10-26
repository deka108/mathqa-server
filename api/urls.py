from api import views

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^education_levels/$', views.EducationLevelList.as_view()),
    url(r'^education_levels/(?P<pk>[0-9]+)/$',
        views.EducationLevelDetail.as_view()),

    url(r'^topics/$', views.TopicList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$',
        views.TopicDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
