from . import views

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^education_levels/$', views.EducationLevelList.as_view()),
    url(r'^education_levels/(?P<pk>[0-9]+)/$',
        views.EducationLevelDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
