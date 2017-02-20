from apiv2.models import Formula
from apiv2.search.utils import formula_extractor as fe
from apiv2.search.utils import formula_features_extractor as ffe


def print_token(text):
    formulas = fe.extract_formulas_from_text(text)

    for formula in formulas:
       print(ffe._generate_mathmlstr(formula))
