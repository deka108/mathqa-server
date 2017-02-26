from apiv2.models import TestFormula, TestFormulaCategory


def update_category(test_formula, categories):
    f_categories = TestFormulaCategory.objects.filter(pk__in=categories)
    test_formula.categories.set(f_categories)


def update_questions(test_formula, questions):
    test_formula.questions = questions


def get_questions(formula_questions):
    return set(q.strip() for q in formula_questions.split(","))


def join_questions(questions_list):
    return ", ".join(questions_list)


def insert_test_formula(formula_data):
    try:
        test_formula = TestFormula.objects.get(content=formula_data.get(
            u'content'))
        print("Formula already exists")
        tf_questions = get_questions(test_formula.questions)
        fd_questions = get_questions(formula_data.get(u'questions'))
        questions = tf_questions | fd_questions
        test_formula.questions = join_questions(questions)
        test_formula.save()
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


def update_test_formula(formula_data):
    try:
        test_formula = TestFormula.objects.get(id=formula_data.get(u'id'))

        content = formula_data.get(u'content')
        questions = formula_data.get(u'questions')
        categories = formula_data.get(u'categories')

        test_formula.content = content
        test_formula.questions = questions
        update_category(test_formula, categories)
        test_formula.save()

        return True
    except TestFormula.DoesNotExist:
        return False


def delete_test_formula(formula_data):
    try:
        TestFormula.objects.get(id=formula_data.get(u'id')).delete()
        return True
    except TestFormula.DoesNotExist:
        return False


def delete_test_formulas(formula_ids):
    for fid in formula_ids:
        TestFormula.objects.filter(id=fid).delete()
