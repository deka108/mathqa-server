from apiv2.models import TestFormulaCategory, FormulaCategory, TestFormula, \
    Formula, Question
from apiv2.search.test_fsearch.utils import test_formula_util as tfu


def insert_formula_category():
    formula_categories = TestFormulaCategory.objects.all()
    for fc in formula_categories:
        new_fc = FormulaCategory(name=fc.name)
        new_fc.save()


def insert_formula():
    formulas = TestFormula.objects.all()
    Formula.objects.delete()

    for f in formulas:
        formula = Formula(
            content=f.content,
            status=False
        )
        formula.save()

        f_categories = f.categories.all()

        for c in f_categories:
            formula.categories.add(
                FormulaCategory.objects.get(name=c.name).name)

        if f.questions:
            question_ids = tfu.get_questions(f.questions)
            questions = Question.objects.filter(pk__in=question_ids)
            for q in questions:
                formula.questions.add(q)

        formula.save()