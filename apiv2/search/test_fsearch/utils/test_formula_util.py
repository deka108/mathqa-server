from apiv2.models import TestFormula, TestFormulaCategory

def update_category(test_formula, categories):
    for category in categories:
        f_cat = TestFormulaCategory.objects.get(pk=category)
        if f_cat:
            test_formula.categories.add(f_cat)


def update_questions(test_formula, questions):
    test_formula.questions = questions


def insert_test_formula(formula_data):
    try:
        TestFormula.objects.get(content=formula_data.get(u'content'))
        print("Formula already exists")
        return False
    except TestFormula.DoesNotExist:
        test_formula = TestFormula(content=formula_data.get(u'content'),
                                   questions=formula_data.get(u'questions'))
        test_formula.save()
        update_category(test_formula, formula_data.get(u'categories'))
        test_formula.save()
        return True


def insert_test_formulas(formula_datas):
    for formula_data in formula_datas:
        insert_test_formula(formula_data)


def delete_test_formulas(formula_ids):
    for fid in formula_ids:
        TestFormula.objects.filter(id=fid).delete()
