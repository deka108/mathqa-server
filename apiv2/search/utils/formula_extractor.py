import re

DOUBLE_DOLLAR_NOTATION = re.compile(r'\$\$([^\$]+)\$\$')
PAREN_NOTATION = re.compile(r'\\\(([^\(]+)\\\)')
BRACKET_NOTATION = re.compile(r'\\\[([^\[]+)\\\]')
SINGLE_DOLLAR_NOTATION = re.compile(r'\$([^\$]+)\$')
LEFTP_PATTERN = re.compile(r'\(')
RIGHTP_PATTERN = re.compile(r'\)')
LEFTB_PATTERN = re.compile(r'\[')
RIGHTB_PATTERN = re.compile(r'\]')
MATHRM_PATTERN = re.compile(r'\\mathrm')


def extract_latex_from_raw_query(text):
    if text[0] == "$" and text[-1] == "$":
        return text.strip("$")
    return text


def extract_formulas_from_text(text):
    """
    Extract latex formulas from a question.

    Args:
        question_id: question id.

    Returns:
        List of latex formulas.
    """
    latex_formulas = []
    latex_formulas += DOUBLE_DOLLAR_NOTATION.findall(text)
    latex_formulas += PAREN_NOTATION.findall(text)
    latex_formulas += BRACKET_NOTATION.findall(text)
    latex_formulas = list(set(latex_formulas))

    return _escape_bracket_parens_mathrm(latex_formulas)


def _escape_bracket_parens_mathrm(formulas):
    for i in range(len(formulas)):
        formula = formulas[i]
        formula = MATHRM_PATTERN.sub('', formula)
        formulas[i] = formula
    return formulas