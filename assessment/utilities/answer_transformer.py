"""
# Name:           check_answer_api/utilities/answer_transformer.py
# Description:
# Created by:     Unknown
# Date Created:   ---
# Last Modified:  Dec 2, 2016
# Modified by:    Martinus Alexander
"""

import re
import pattern_dictionary_all
import pattern_dictionary_standardize_mathquill

"""
Helper method to make sure that the process is recursive.
"""


def replace_recursive(pattern, repl, expression):
    count = 1
    expr = expression[:]
    while count != 0:
        expr, count = re.subn(pattern, repl, expr)
    return expr


"""
Transform expression in Latex format into ASCII (Sympy) format.
Approach: Recursive transformation using regular expression.
"""


def transform_latex_to_sympy(expression, mode="Other"):
    # Remove all spaces
    expr = expression.replace(' ', '')
    # Remove all '*' because it makes the dictionary fails (the dictionary
    # assumes no '*' entered)
    expr = expr.replace('*', '')
    # Makes all character to lowercase (uppercase variable name in Sympy is
    # considered as function)
    expr = expr.lower()
    if mode.lower() == "mathquill only":
        for pattern, repl in pattern_dictionary_standardize_mathquill.rules:
            expr = replace_recursive(pattern, repl, expr)
    else:
        for pattern, repl in pattern_dictionary_all.rules:
            expr = replace_recursive(pattern, repl, expr)
    return expr
