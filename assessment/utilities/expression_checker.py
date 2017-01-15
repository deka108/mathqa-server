"""
# Name:           check_answer_api/utilities/expression_checker.py
# Description:
# Created by:     Unknown
# Date Created:   ---
# Last Modified:  Dec 1, 2016
# Modified by:    Martinus Alexander
"""

from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import answer_transformer

"""
Compare 2 Latex expressions and return the correctness of the answer.
In between, there is a need to transform the expression in Latex syntax into
ASCII syntax.
"""


def check(x, y):
    x_ascii = answer_transformer.transform_latex_to_sympy(x)
    y_ascii = answer_transformer.transform_latex_to_sympy(y)
    result = evaluate_answer_in_ascii(x_ascii, y_ascii)
    return result


"""
Evaluates the transformed Latex and returns the correctness of the answer.
"""


def evaluate_answer_in_ascii(x, y):
    if x and y:
        try:
            # Check the existence of +- sign or -+ sign
            xPlusMinus = (x.count("pm") + x.count("mp")) > 0
            yPlusMinus = (y.count("pm") + y.count("mp")) > 0
            equal_no_of_pm = (x.count("pm") + x.count("mp")
                              ) == (y.count("pm") + y.count("mp"))

            if (xPlusMinus or yPlusMinus) and not equal_no_of_pm:
                # Different number of +- and -+ between 2 expressions, then
                # automatically wrong
                return False
            if xPlusMinus and yPlusMinus and equal_no_of_pm:
                # Handle +-
                # +- needs to be handled manually since Sympy cannot handle +-
                # nor - +
                # Split the expression into 2 parts, one contains + whereas the
                # other contains -
                x1 = parse_expr(x.replace('pm', '+').replace('mp', '-'))
                x2 = parse_expr(x.replace('pm', '-').replace('mp', '+'))
                y1 = parse_expr(y.replace('pm', '+').replace('mp', '-'))
                y2 = parse_expr(y.replace('pm', '-').replace('mp', '+'))
                # Check individually
                z1 = simplify(x1 - y1)
                z2 = simplify(x2 - y2)
                # Both must be correct
                return (z1 == 0 and z2 == 0)
            elif not xPlusMinus and not yPlusMinus:
                # No +- nor -+ sign found, so handle the expression normally
                x = parse_expr(x)
                y = parse_expr(y)
                z = simplify(x - y)
                return(z == 0)
        except SyntaxError:
            return False
    else:
        # No answer specified
        return False
