from django.contrib import admin
from django.contrib.admin import ModelAdmin

from meas_models.models import *


class TopicAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'order')
    list_editable = ('name', 'description', 'order')


admin.site.register(Topic, TopicAdmin)


class ConceptAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_editable = ('name', 'description')


admin.site.register(Concept, ConceptAdmin)


class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'content', 'source', 'difficulty_level')
    list_editable = ('content', 'source', 'difficulty_level')


admin.site.register(Question, QuestionAdmin)
