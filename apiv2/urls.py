from apiv2 import views
from apiv2 import views_hyperlink as hviews

from django.contrib.auth import views as auth_views
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
router.register(r'papers', views.PaperViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'test_questions', views.TestQuestionViewSet)
router.register(r'solutions', views.SolutionViewSet)
router.register(r'formulas', views.FormulaViewSet)
router.register(r'formula_indexes', views.FormulaIndexViewSet)
router.register(r'test_formulas', views.TestFormulaViewSet)
router.register(r'test_formula_categories', views.TestFormulaCategoryViewSet)
router.register(r'test_formula_indexes', views.TestFormulaIndexViewSet)
router.register(r'keypoints', views.KeyPointViewSet)
router.register(r'keywords', views.KeywordViewSet)

router.register(r'heducation_levels', hviews.EducationLevelViewSet)
router.register(r'hsubjects', hviews.SubjectViewSet)
router.register(r'htopics', hviews.TopicViewSet)
router.register(r'hconcepts', hviews.ConceptViewSet)
router.register(r'hsubconcepts', hviews.SubconceptViewSet)
router.register(r'hpapersets', hviews.PapersetViewSet)
router.register(r'hpapers', hviews.PaperViewSet)
router.register(r'hquestions', hviews.QuestionViewSet)
router.register(r'hsolutions', hviews.SolutionViewSet)
router.register(r'hformulas', hviews.FormulaViewSet)
router.register(r'hformula_indexes', hviews.FormulaIndexViewSet)
router.register(r'hkeypoints', hviews.KeyPointViewSet)
router.register(r'hkeywords', hviews.KeywordViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', views.schema_view),
    url(r'^formula/reindex_all$', views.reindex_all_formula),
    url(r'^formula/reindex_test$', views.reindex_test_formula),
    url(r'^check_token/(?P<concept_id>[0-9]+)$', views.check_token),
    url(r'^check_tokens/$', views.check_token_questions),
    url(r'^check_mathml/$', views.check_mathml_str),
    url(r'^check_formula_token/$', views.check_formula_token),
    url(r'^create_update_test_formula/$', views.create_update_test_formula),
    url(r'^delete_test_formula/$', views.delete_test_formula),
    url(r'^reindex_test_formula/$', views.reindex_test_formula),
    url(r'^search_test_formula/$', views.search_test_formula),
    # account
    # url(r'^register/$', ),
    # url(r'^logout/$', ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^login/', auth_views.login),
    url(r'^logout/', auth_views.logout),
]
