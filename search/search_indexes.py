# from django.utils import timezone
# from haystack import indexes
# from meas_models.models import *


# class QuestionIndex(indexes.SearchIndex, indexes.Indexable):

#     text = indexes.CharField(document=True, use_template=True)
#     question_type = indexes.CharField(model_attr="question_type")
#     used_for = indexes.CharField(model_attr="used_for")
#     mark = indexes.IntegerField(model_attr="mark")
#     difficulty_level = indexes.CharField(model_attr="difficulty_level")
#     respone_type = indexes.CharField(model_attr="respone_type")
#     content = indexes.CharField(model_attr="content")
#     solution = indexes.CharField(model_attr="solution")
#     answer = indexes.CharField(model_attr="answer")

#     concept = indexes.CharField(model_attr="concept")
#     keypoint = indexes.CharField(model_attr="keypoint")

#     formulas = MultiValuedField()

#     def get_model(self):
#         return Question

#     def prepare_formulas(self, obj):
#         # many to many
#         return [formula.id for formula in obj.formula_set.active()]

#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()
