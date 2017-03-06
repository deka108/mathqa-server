from itertools import chain
from apiv2.models import Formula, FormulaCategory, Question


def update_category(formula, categories):
    f_categories = FormulaCategory.objects.filter(pk__in=categories)
    formula.categories.set(f_categories)


def update_questions_by_ids(formula, question_ids):
    update_questions(formula, get_questions_by_ids(question_ids))


def update_questions(formula, questions):
    formula.questions.set(questions)


def get_questions_by_ids(question_ids):
    q_ids = [q.strip() for q in question_ids.split(",")]
    return Question.objects.filter(pk__in=q_ids)


def insert_formula(formula_data):
    try:
        formula = Formula.objects.get(content=formula_data.get(u'content'))
        tf_questions = formula.questions
        fd_questions = get_questions_by_ids(formula_data.get(u'questions'))
        questions = set(chain(tf_questions, fd_questions))

        update_questions(formula, questions)

        print("Formula already exists")

        return False
    except Formula.DoesNotExist:
        new_formula = Formula(content=formula_data.get(u'content'))
        new_formula.save()
        update_questions_by_ids(new_formula, formula_data.get(u'questions'))
        update_category(new_formula, formula_data.get(u'categories'))
        return True


def insert_formulas(formula_datas):
    for formula_data in formula_datas:
        insert_formula(formula_data)


def update_formula(formula_data):
    try:
        formula_obj = Formula.objects.get(id=formula_data.get(u'id'))

        content = formula_data.get(u'content')
        question_ids = formula_data.get(u'questions')
        categories = formula_data.get(u'categories')

        formula_obj.content.set(content)
        update_questions_by_ids(formula_obj, question_ids)
        update_category(formula_obj, categories)

        return True
    except Formula.DoesNotExist:
        return False


def delete_formula(formula_data):
    try:
        Formula.objects.get(pk=formula_data.get(u'id')).delete()
        return True
    except Formula.DoesNotExist:
        return False


def delete_formulas(formula_ids):
    Formula.objects.filter(pk__in=formula_ids).delete()
