"""
# Name:           check_answer_api/utilities/pattern_dictionary_standardize_mathquill.py
# Description:
# Created by:     Martinus Alexander
# Date Created:   Dec 2, 2016
# Last Modified:  Dec 2, 2016
# Modified by:    Martinus Alexander
"""

rules = [

    #+? denotes not-greedy search ref: (http://stackoverflow.com/a/1919995)

    # Preprocessing for Mathquill
    #(r'\[', r'('), #left bracket
    #(r'\]', r')'), #right bracket

    # for Mathquill
    (r'\\operatorname\{cosec\}', '\\csc'),
    (r'\\cdot', ''),  # multiply sign indicated by circle dot
    (r'\\\times', ''),  # multiply sign indicated by cross
    (r'\^\{\\circ\}', '/180*\\pi'),  # degree to radian conversion
    (r'\\\degree', '/180*\\pi'),  # degree to radian conversion
    # trigonometric and logarithmic with power but without bracket
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^([0-9A-Za-z])', r'\\\1^{\2}'),
    # trigonometric and logarithmic without bracket
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z\^]+)', r'\\\1{\2}'),
    # curly bracket for one-character after power sign
    (r'\^([a-zA-Z0-9])', r'^{(\1)}'),
    # curly bracket for one-character after underscores sign
    (r'\_([a-zA-Z0-9])', r'_{(\1)}'),
    # take back wrong conversion
    (r'\{\^\}', r'^'),  # only cap inside curly bracket

]
