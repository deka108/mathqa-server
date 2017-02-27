import formula_bracket as fb
from apiv2.models import TestFormulaCategory


def insert_formula_categories(reset_formula=False, categories=None):
    if reset_formula:
        TestFormulaCategory.objects.all().delete()

    if not categories:
        categories = fb.FORMULA_CATEGORIES

    for category in categories:
        insert_formula_category(category)


def insert_formula_category(category):
    try:
        TestFormulaCategory.objects.get(name=category)
        print("Category already exists!")
    except TestFormulaCategory.DoesNotExist:
        test_formula_category = TestFormulaCategory(name=category)
        test_formula_category.save()
        print("Formula category created!")


def get_formula_categories():
    return TestFormulaCategory.objects.all()


def rename_formula_category(old_formula, new_formula):
    TestFormulaCategory.objects.get(pk=old_formula).delete()
    insert_formula_category(new_formula)


