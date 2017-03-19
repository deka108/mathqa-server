import re

# CATEGORIES
ABSOLUTE = 'absolute'
DIFFERENTIATION = 'differentiation'
EXPONENTIAL = 'exponential'
FRACTION = 'fraction'
INEQUALITY = 'inequality'
INTEGRAL = 'integral'
LIMIT = 'limit'
LINE_EQUATIONS = 'line equations'
LOGARITHMS = 'logarithms'
POLYNOMIAL = 'polynomial'
SURDS = 'surds'
TRIGONOMETRY = 'trigonometry'
OTHERS = 'others'

ARITHMETICS = 'arithmetic'
RELATIONS = 'relations'
SERIES = 'series'
LIMIT = 'limit'

FORMULA_CATEGORIES = [ABSOLUTE, DIFFERENTIATION, EXPONENTIAL, FRACTION,
                      INEQUALITY, INTEGRAL, LIMIT, LINE_EQUATIONS, LOGARITHMS,
                      OTHERS, POLYNOMIAL, SERIES, SURDS, TRIGONOMETRY]

# Latex
FORMULA_PATTERN = {
    ABSOLUTE: [r'\|'],
    DIFFERENTIATION: [r'\\mathrm', r'd{.+}'],
    EXPONENTIAL: ['e\^\{[a-zA-Z]+\}', 'e\^[a-zA-Z]+', r'\d+\^\{[a-zA-Z]+\}',
                  r'\d+^[a-zA-Z]+'],
    FRACTION: [r'\\frac', r'\bfrac\b', 'fraction'],
    INEQUALITY: ['<', '>', r'\\leq', r'\\le', r'\\geq', r'\\ge'],
    INTEGRAL: [r'\\int'],
    LINE_EQUATIONS: ['line', 'curve'],
    LOGARITHMS: [r'\\log', r'\\ln', r'\\lg', r'\blog\b', r'\bln\b', r'\blg\b'],
    POLYNOMIAL: [r'[a-zA-Z]\^'],
    SERIES: [r'\\sum'],
    LIMIT: [r'\\lim'],
    TRIGONOMETRY: [r'\\sin', r'\\cos', r'\\tan', r'\bsin\b', r'\bcos\b', 
    r'\btan\b', r'\\sec', r'\\cot', r'\\csc', r'\bsec\b', r'\bcot\b', r'\bcsc\b'],
    SURDS: [r'\\sqrt', 'sqrt'],
}


def get_categories(text):
    categories = []

    for category in FORMULA_PATTERN:
        combined = "(.*" + ".*)|(.*".join(FORMULA_PATTERN[category]) + ".*)"

        if re.match(combined, text):
            categories.append(category)

    return categories

