from apiv2.search.test_fsearch import util
from apiv2.models import TestQuestion, Question


def insert_test_questions(reset=True):
    test_questions = util.read_test_questions_mids()

    if reset:
        TestQuestion.objects.all().delete()

    for topic in test_questions:
        print(topic)
        for test_id in test_questions[topic]:
            question = Question.objects.get(pk=test_id)
            new_test_question = TestQuestion(
                id=question.id,
                category=topic,
                marks=question.marks,
                difficulty_level=question.difficulty_level,
                source = question.source,
                content=question.content,
                concept=question.concept,
                subconcept=question.subconcept,
                paper = question.paper
            )
            new_test_question.save()