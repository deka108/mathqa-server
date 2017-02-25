import formula_bracket as fb
from apiv2.models import TestFormulaCategory


def insert_formula_category(reset_formula=False, categories=None):
    if (reset_formula):
        TestFormulaCategory.objects.delete()

    if not categories:
        categories = fb.FORMULA_CATEGORIES

    for category in categories:
        try:
            TestFormulaCategory.objects.get(
                name=category)
            print("Category already exists!")
        except TestFormulaCategory.DoesNotExist:
            test_formula_category = TestFormulaCategory(name=category)
            test_formula_category.save()
            print("Formula category created!")


def get_formula_categories():
    return TestFormulaCategory.objects.all()



