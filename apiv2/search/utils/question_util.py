from apiv2.models import Question
from apiv2.search.utils import text_util as tu
from apiv2.search.utils import formula_bracket as fb


def preprocess_questions(english=True, stem=False):
    all_questions = Question.objects.all()
    all_questions.update(content_cleaned_text='')
    for question in all_questions:
        preprocessed_text = tu.preprocess(question.content,
                                          english=english,
                                          stem=stem)
        question.content_cleaned_text = preprocessed_text
        question.save()
        print("Preprocessed text of question: %s" % question.id)


def update_formula_category():
    all_questions = Question.objects.all()
    for question in all_questions:
        question.formula_categories = fb.get_categories(question.content)
        question.save()


def update_question(question_data):
    try:
        question_obj = Question.objects.get(id=question_data.get(u'id'))
        content = question_data.get(u'content')

        question_obj.content = content
        question_obj.save()

        return question_obj
    except Question.DoesNotExist:
        return False