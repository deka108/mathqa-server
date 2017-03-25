operator_terms = tuple()

# binary operators
operator_terms += ('pm', 'times', 'div', 'ast', 'dot', 'cap', 'cup',
                    'vee', 'wedge', '+', '-', 'times', 'plus',
                    u'\xb1', u'\xd7', u'\xf7', u'\u2212', u'\u2215',
                    u'\u2216', u'\u2217', u'\u2218', u'\u2219', u'\u221D',
                    u'\u221E', u'\u221F', u'\u2220', u'\u2225', u'\u2227',
                    u'\u2228', u'\u2229', u'\u222A')

# relation operators
operator_terms += ('leq', 'geq', 'equiv', 'nequiv', 'models', 'sim',
                    'simeq', 'mid', 'parallel', 'subset', 'supset',
                    'approx', 'subseteq', 'supseteq', 'cong', 'join', 'neq',
                    'proptoin', '=', '<', '>',
                    u'\u2260', u'\u2261', u'\u2262', u'\u2263', u'\u2264',
                    u'\u2265', u'\u2266', u'\u2267', u'\u2243',
                    u'\u2282', u'\u2283', u'\u2284', u'\u2285', u'\u2286',
                    u'\u2287', u'\u2288', u'\u2289', u'\u228A', u'\u228B',
                    u'\u2A1D', u'\u2223', u'\u2239', u'\u223C', u'\u223D',
                    u'\u2242', u'\u2243', u'\u2244', u'\u2245', u'\u2246',
                    u'\u2247', u'\u2248', u'\u2249', u'\u224A', u'\u224B',
                    u'\u224C', '!')

# punctuation operators
operator_terms += (',', 'colon', 'ldotp', 'cdotp', u'\u2234', u'\u2235',
                    u'\u2236', u'\u2237')

# arrow operators
operator_terms += ('leftarrow', 'Leftarrow', 'rightarrow', 'Rightarrow',
                    'leftrightarrow', 'Leftrightarrow', 'leftharpoonup',
                    'leftharpoondown', 'rightleftharpoons',
                    'rightharpoonup', 'rightharpoondown', 'mapsto')
# miscellaneous operators
operator_terms += ('ldots', 'cdots', 'vdots', 'ddots', 'forall', 'infty',
                    'exists', 'nabla', 'neg', 'triangle', 'angle', 'bot',
                    'prime', 'emptyset', u'\u2026')
# vars sized operators
operator_terms += ('prod', 'coprod', 'bigcap', 'bigcup',
                    'bigodot', 'bigotimes', 'bigoplus')
# delimiter operators
operator_terms += ('(', ')', 'uparrow', 'Uparrow', '[', ']',
                    'downarrow', 'Downarrow', '{', '}', 'updownarrow',
                    'Updownarrow', 'lfloor', 'rfloor', 'lceil', 'rceil',
                    'langle', 'rangle', '/', 'backslash', '|', 'lgroup',
                    'rgroup', '\\', '.', '\'')
# other operators
operator_terms += ('widetilde', 'widehat', 'overleftarrow',
                    'overrightarrow', 'overline', 'underline',
                    'overbrace', 'underbrace')

function_terms = ('arccos', 'cos', 'csc', 'exp', 'limsup', 'min', 'sinh',
    'arcsin', 'cosh', 'deg', 'gcd', 'lg', 'ln', 'sup',
    'arctan', 'cot', 'det', 'lim', 'sin', 'log', 'sec',
    'tan', 'arg', 'coth', 'dim', 'inf', 'liminf', 'max',
    'tanh', 'int',  'sum',  'sqrt', 'frac', 'sum',
    u'\u2211', u'\u222B', u'\u221A')