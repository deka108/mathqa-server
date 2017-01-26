from apiv2 import views

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.SimpleRouter()

router.register(r'education_levels', views.EducationLevelViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'concepts', views.ConceptViewSet)
router.register(r'subconcepts', views.SubconceptViewSet)
router.register(r'papersets', views.PapersetViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'solutions', views.SolutionViewSet)
router.register(r'formulas', views.FormulaViewSet)
router.register(r'formula_indexes', views.FormulaIndexViewSet)
router.register(r'keypoints', views.KeyPointViewSet)
router.register(r'keywords', views.KeywordViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', views.schema_view),
    url(r'^formula/reindex_all$', views.reindex_all_formula),

    # search
    url(r'^dsearch/$', views.search_text_db, name="search_db_text"),
    url(r'^fsearch/$', views.search_formula, name="search_formula"),
    url(r'^csearch/$', views.search_formula_cluster,
        name="search_formula_cluster"),

    # real vs sample questions
    # url(r'^sample_questions'),
    # url(r'^real_questions'),

    # account
    # url(r'^register/$', ),
    # url(r'^logout/$', ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
]
