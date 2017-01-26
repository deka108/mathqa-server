"""
# Name:           check_answer_api/utilities/pattern_dictionary_all.py
# Description:
# Created by:     Martinus Alexander
# Date Created:   Sep 2, 2016
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
    #(r'\^([a-zA-Z])', r'^{(\1)}'), #symbol as the power
    (r'\\frac\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)/(\2)'),  # fraction with expression inside
    # trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}\\left\(([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)\\right\)', r'\\\1^{\2}{\3}'),
    # trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}\\left\(([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)\\right\)', r'\\\1^{\2}{\3}'),
    # trigonometric and logarithmic
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\\left\(([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)\\right\)', r'\\\1{\2}'),
    # single trigonometric expression with power with symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}([0-9A-Za-z]*)(\\alpha|\\beta|\\gama|\\lambda|\\theta|\\mu|\\sigma|\\pi)([\+\-\\]?)', r'\\\1^{\2}{\3\4}\5'),
    # single trigonometric expression with symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z]*)(\\alpha|\\beta|\\gama|\\lambda|\\theta|\\mu|\\sigma|\\pi)([\+\-\\]?)',
     r'\\\1{\2\3}\4'),
    # single trigonometric expression without power with symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}([0-9A-Za-z]+)([\+\-\\]?)', r'\\\1^{\2}{\3}\4'),
    # single trigonometric expression without symbol
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z]+)([\+\-\\]?)',
     r'\\\1{\2}\3'),
    #(r'\\left\(()\\right\)\^', r'{\1}^'), # Mathematical function as the base
    (r'(\d+|[a-zA-Z])\^\{', r'{\1}^{'),  # variable or constant as the base
    # absolute function as the base
    (r'\\left\|([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)\\right\|\^', r'{|\1|}^'),
    #(r'\\left\(([a-zA-Z0-9\+\-]+)\\right\)\^', r'{\1}^'), #expression inside bracket as the base
    # expression inside bracket as the base
    (r'\\left\(([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+?)\\right\)\^', r'{\1}^'),
    # take back wrong conversion
    # symbol
    (r'\\(p|alph|bet|gamm|thet|lambd|m|sigm)\{([a-zA-Z])\}', r'{\\\1\2}'),
    # trigonometric operator #1
    (r'(sin|cos|tan|cot|sec|csc|log|ln)\{\^\}', r'\1^'),
    (r'(si|co|ta|se|cs|lo|l)\{([a-zA-Z])}',
     r'\1\2'),  # trigonometric operator #2

    # bracket
    (r'\\left\(', r'('),  # left bracket
    (r'\\right\)', r')'),  # right bracket
    (r'\\left\{', r'{'),  # left bracket
    (r'\\right\}', r'}'),  # right bracket
    (r'\\left\[', r'('),  # left bracket
    (r'\\right\]', r')'),  # right bracket
    #(r'\\left\|', r'{|'), #left bracket
    #(r'\\right\|', r'|}'), #right bracket
    (r'\[', r'('),  # left bracket
    (r'\]', r')'),  # right bracket
    #(r'\|', r'|'), #absolute

    # preprocess of plus minus symbol
    (r'\\pm', r'(pm)'),
    (r'\\mp', r'(mp)'),

    (r'\{\|([0-9A-Za-z\+\-\*\/\\\(\)\.\^\{\}]+?)\|\}',
     r'|\1|'),  # absolute function
    # absolute function (added from Mathquill)
    (r'(\\left)?\|([0-9A-Za-z\+\-\*\/\\\(\)\.\^\{\}]+?)(\\right)?\|', r'{abs(\2)}'),
    (r'(\d+\.?\d*\.?\d*|\}|\))([a-zA-Z])',
     r'\1*\2'),  # coefficient of a variable
    # cofficient of pi (alphanumeric only)
    (r'([a-zA-Z]|\d+\.?\d*)\\pi', r'\1*\pi'),
    (r'(\d+)\!', r'factorial(\1)'),  # factorial
    (r'\\frac\{([0-9a-zA-Z\.\+\-]+|\\pi)\}\{([0-9a-zA-Z\.\+\-]+|\\pi)\}',
     r'(\1)/(\2)'),  # fraction with simple expression
    (r'(\d+\.?\d*|[A-Za-z]|\\pi)\^(\d+\.?\d*|[A-Za-z]|\\pi)',
     r'(\1)**(\2)'),  # power without bracket at all
    (r'\\int\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)d([a-zA-Z]+)\}',
     r'integrate(\1, \2)'),  # indefinite integration
    (r'\\int\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'integrate(\1, x)'),  # indefinite integration
    # Definite integration parsing needs to have 2 steps in order to reduce error
    # Definite integration parsing step #1
    (r'\\int\_\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}',
     r'\int_from{\1}_to{\2}'),  # definite integration
    (r'\\int\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\_\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}',
     r'\int_from{\2}_to{\1}'),  # definite integration
    #(r'\}(.+)', r'}{\1}'), #adding curly bracket for integration(added for Matquill)
    (r're\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}', r're(\1)'),  # complex number
    (r'im\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}', r'im(\1)'),  # complex number
    (r'e\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'exp(\1)'),  # exponent with power
    #(r'([0-9]+|[A-Za-z])\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'(\1)**(\2)'), # power with curly bracket in its power only
    (r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\^([0-9]+|[A-Za-z])',
     r'(\1)**(\2)'),  # power with curly bracket in its base only
    (r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)**(\2)'),  # power with curly bracket
    (r'\)\^(\d+)', r')*\1'),  # nested power
    (r'\\sqrt\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'sqrt(\1)'),  # square root
    (r'\\frac\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)/(\2)'),  # fraction with expression inside
    # trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}', r'\1(\3)**(\2)'),
    # trigonometric and logarithmic
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'\1(\2)'),
    # power to handle mathematical function in the form e.g. (ln x)^2 (added
    # for Mathquill)
    (r'\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'(\1)**(\2)'),
    (r'\\frac\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'(\1)/(\2)'),  # fraction with expression inside
    # Sqrt must be done again in order to handle sqrt of trigonometric function
    (r'\\sqrt\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'sqrt(\1)'),  # square root
    # exponent to handle complex number
    (r'e\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'exp(\1)'),
    # exponent to handle complex number
    (r'e\^\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}', r'exp(\1)'),
    (r'i\(', r'i*('),  # complex number as coefficient
    (r'\)\\pi', r')*\pi'),  # cofficient of pi
    (r'([0-9a-zA-Z]+|\\pi|\))(sin|cos|tan|cot|sec|csc|log|ln)',
     r'\1*\2'),  # coefficient of trigonometric and logarithmic function
    # coefficient of expression inside bracket
    (r'(\d+|[a-zA-Z]|\\pi)\(',  r'\1*('),
    (r'([0-9a-zA-Z]+|\\pi|\)+)exp',  r'\1*exp'),  # coefficient of exponent
    (r'([0-9a-zA-Z]+|\\pi|\)+)sqrt',
     r'\1*sqrt'),  # coefficient of square root
    (r'(\)|\d+)(\\[a-zA-Z]+)', r'\1*\2'),  # coefficient of a symbol
    # pi as a coefficient of expression without bracket
    (r'\\pi(\\|\()', r'\pi*\1'),
    (r'\\pi\(', r'\pi*('),  # pi as a coefficient of expression in bracket
    (r'\)\(', r')*('),  # 2 consecutive parentheses
    (r'\)(\d+)', r')*\1'),  # digits after parentheses

    # Trigonometry and logarithm (added for Mathquill)
    # trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)\^\{(\S+)\}([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)', r'\1(\3)**(\2)'),
    # trigonometric and logarithmic with power
    (r'\\(sin|cos|tan|cot|sec|csc|log|ln)([0-9A-Za-z\+\-\^\/\\\(\)\{\}\.]+)', r'\1(\3)**(\2)'),

    # Definite integration parsing step #2
    (r'\\int_from\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}_to\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)d([a-zA-Z]+)\}',
     r'integrate(\3, (\4, \1, \2))'),  # definite integration, added for Mathquill
    (r'\\int_from\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}_to\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)',
     r'integrate(\3, (x, \1, \2))'),  # definite integration, added for Mathquill
    (r'\\int_from\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}_to\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)d([a-zA-Z]+)\}',
     r'integrate(\3, (\4, \1, \2))'),  # definite integration
    (r'\\int_from\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}_to\{([0-9A-Za-z\+\-\*\/\\\(\)\.]+)\}\{([0-9A-Za-z\+\-\*\/\\\(\)\.\^]+)\}',
     r'integrate(\3, (x, \1, \2))'),  # definite integration

    (r'\\piintegrate', r'\pi*integrate'),  # pi as a coefficient of integration

    # backup for trigonometric, logarithmic, exponent function which was added
    # with '*'
    (r'(sin|cos|tan|cot|sec|csc|log|ln|exp|sqrt|integrate|re|im|factorial|abs)\*', r'\1'),

    # not
    (r'not', r'no'),

    # pi
    (r'\\pi', r'pi'),

    # symbol
    (r'\\alpha', r'a'),
    (r'\\beta', r'b'),
    (r'\\gama', r'g'),
    (r'\\theta', r't'),
    (r'\\lambda', r'l'),
    (r'\\mu', r'm'),
    (r'\\sigma', r's'),

    # postprocess of plus minus symbol
    (r'\*?\(pm\)\*?', r'pm'),
    (r'\*?\(mp\)\*?', r'mp'),

    # Unnecessary curly bracket
    (r'\{', r'('),
    (r'\}', r')'),


    #(r'\)\s([\\\w]+)',r')*\1'), #closing parentheses + symbols
]
