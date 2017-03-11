from haystack import indexes
from haystack.fields import CharField, IntegerField, BooleanField, \
    MultiValueField

from apiv2.models import Question


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = CharField(document=True)
    id = CharField(model_attr='id')
    question_type = CharField(model_attr = 'question_type')
    used_for = CharField(model_attr = 'used_for')
    marks = IntegerField(model_attr = 'marks')
    difficulty_level = CharField(model_attr = 'difficulty_level')
    response_type = CharField(model_attr = 'response_type')
    source = CharField(model_attr = 'source')
    content = CharField(model_attr = 'content')
    content_cleaned_text = CharField(model_attr = 'content_cleaned_text')
    is_sample = BooleanField(model_attr = 'is_sample')

    concept = CharField(model_attr = 'concept')
    subconcept = CharField(model_attr = 'subconcept')
    paper = CharField(model_attr = 'paper')

    keypoints = MultiValueField()
    keywords = MultiValueField()

    def get_model(self):
        return Question


    def prepare_keypoints(self, obj):
        return [keypoint.pk for keypoint in obj.keypoints.all()]


    def prepare_keywords(self, obj):
        return [keyword.pk for keyword in obj.keywords.all()]


    def index_queryset(self, using=None):
        return self.get_model().objects.all()