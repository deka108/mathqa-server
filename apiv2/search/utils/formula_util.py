from itertools import chain
from apiv2.models import Formula, FormulaCategory, Question
from apiv2.search.utils import formula_bracket as fb


def init_formula_categories():
    FormulaCategory.objects.all().delete()
    update_formula_categories()


def update_formula_categories():
    for category in fb.FORMULA_CATEGORIES:
        try:
            FormulaCategory.objects.get(name=category)
        except FormulaCategory.DoesNotExist:
            new_category = FormulaCategory(name=category)
            new_category.save()
            print("new category created")


def update_category(formula, categories):
    if categories:
        f_categories = FormulaCategory.objects.filter(pk__in=categories)
        formula.categories.set(f_categories)


def update_questions_by_ids(formula, question_ids):
    update_questions(formula, get_questions_by_ids(question_ids))


def update_questions(formula, questions):
    if questions:
        formula.questions.set(questions)


def get_questions_by_ids(question_ids):
    if question_ids:
        if isinstance(question_ids, list):
            q_ids = question_ids
        else:
            q_ids = [q.strip(" \"") for q in question_ids.strip("[]").split(",")]
        print(q_ids)
        return Question.objects.filter(pk__in=q_ids)


def insert_formula(formula_data):
    try:
        formula = Formula.objects.get(content=formula_data.get(u'content'))
        tf_questions = formula.questions
        fd_questions = get_questions_by_ids(formula_data.get(u'questions'))

        if fd_questions:
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

        formula_obj.content = content
        formula_obj.save()

        update_questions_by_ids(formula_obj, formula_data.get(u'questions'))
        update_category(formula_obj, formula_data.get(u'categories'))

        return formula_obj
    except Formula.DoesNotExist:
        return False


def delete_formula(formula_data):
    try:
        if formula_data:
            deleted_formula = Formula.objects.get(pk=formula_data.get(
                u'id'))
            deleted_formula.delete()
            return deleted_formula
        raise Formula.DoesNotExist()
    except Formula.DoesNotExist:
        return False


def delete_formulas(formula_ids):
    Formula.objects.filter(pk__in=formula_ids).delete()
