from django.contrib import admin

from meas_models.models import *


class EducationLevelAdmin(admin.ModelAdmin):
    pass


class SubjectAdmin(admin.ModelAdmin):
    pass


class TopicAdmin(admin.ModelAdmin):
    pass


class ConceptAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class PartAdmin(admin.ModelAdmin):
    pass


class SubPartAdmin(admin.ModelAdmin):
    pass


class TestAdmin(admin.ModelAdmin):
    pass


class TestQuestionAdmin(admin.ModelAdmin):
    pass


class ProficiencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(EducationLevel, EducationLevelAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(SubPart, SubPartAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TestQuestion, TestQuestionAdmin)
admin.site.register(Proficiency, ProficiencyAdmin)
