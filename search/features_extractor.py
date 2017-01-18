"""Extracts features from formula."""
from tempfile import TemporaryFile

import xml.etree.ElementTree as ET
import HTMLParser
import latex2mathml.converter as l2m
import locale

htmlparser = HTMLParser.HTMLParser()


def write_dom_to_tempfile(root):
    """
    Writes XML into a temporary file.

    Args:
        root: the root of MathML DOM tree.

    Returns:
        Temporary file of the MathML tree,
    """

    tree = ET.ElementTree(root)
    tempfile = TemporaryFile(suffix='.xml')
    tree.write(tempfile)
    tempfile.seek(0)
    return tempfile


def print_dom_tree(domtree):
    """
    Prints DOM tree content.

    Args:
        domtree: a MathML DOM tree.
    """
    for elt in domtree.iter():
        print("%s: '%s'" % (elt.tag, elt.text))


def is_operator_or_function(term):
    """
    Checks if the term is a LaTeX mathematical operator or function.

    Source: http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html

    Args:
        term: string to be checked.

    Returns:
        True if the term is a mathematical operator, False otherwise.
    """
    operator_terms = tuple()

    # binary operators
    operator_terms += ('pm', 'times', 'div', 'ast', 'dot', 'cap', 'cup',
                       'vee', 'wedge', '+', '-', 'times', 'plus')
    # relation operators
    operator_terms += ('leq', 'geq', 'equiv', 'models', 'sim', 'simeq',
                       'mid', 'parallel', 'subset', 'supset', 'approx',
                       'subseteq', 'supseteq', 'cong', 'join', 'neq', 'propto'
                                                                      'in',
                       '=', '<', '>')
    # punctuation operators
    operator_terms += (',', 'colon', 'ldotp', 'cdotp')
    # arrow operators
    operator_terms += ('leftarrow', 'Leftarrow', 'rightarrow', 'Rightarrow',
                       'leftrightarrow', 'Leftrightarrow', 'leftharpoonup',
                       'leftharpoondown', 'rightleftharpoons',
                       'rightharpoonup', 'rightharpoondown', 'mapsto')
    # miscellaneous operators
    operator_terms += ('ldots', 'cdots', 'vdots', 'ddots', 'forall', 'infty',
                       'exists', 'nabla', 'neg', 'triangle', 'angle', 'bot',
                       'prime', 'emptyset')
    # vars sized operators
    operator_terms += ('sum', 'prod', 'coprod', 'int', 'bigcap', 'bigcup',
                       'bigodot', 'bigotimes', 'bigoplus')
    # delimiter operators
    operator_terms += ('(', ')', 'uparrow', 'Uparrow', '[', ']',
                       'downarrow', 'Downarrow', '{', '}', 'updownarrow',
                       'Updownarrow', 'lfloor', 'rfloor', 'lceil', 'rceil',
                       'langle', 'rangle', '/', 'backslash', '\\|', 'lgroup',
                       'rgroup', '\\', '.', '\'')
    # other operators
    operator_terms += ('widetilde', 'widehat', 'overleftarrow',
                       'overrightarrow', 'overline', 'underline',
                       'overbrace', 'underbrace', 'sqrt', 'frac')

    return is_function(term) or term.endswith(operator_terms) or term == 'e'


def is_function(term):
    """
    Checks if the term is a LaTeX mathematical function.

    Source: http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html

    Args:
        term: string to be checked.

    Returns:
        True if the term is a mathematical function, False otherwise.
    """
    function_terms = ('arccos', 'cos', 'csc', 'exp', 'limsup', 'min', 'sinh',
                       'arcsin', 'cosh', 'deg', 'gcd', 'lg', 'ln', 'sup',
                       'arctan', 'cot', 'det', 'lim', 'log', 'sec', 'tan',
                       'arg', 'coth', 'dim', 'inf', 'liminf', 'max', 'sin',
                       'tanh')
    return term.endswith(function_terms)


def generate_features(latex_str):
    """
    Generates five formula features from a formula written as LaTeX string.

    Args:
        latex_str: formula string in latex format.

    Returns:
        Five tuples corresponding to in order semantic terms, sorted semantic
        terms, structural features, constant features and variable features.

    """
    mathml_str = generate_mathmlstr(latex_str)
    dom_tree = construct_domtree(mathml_str)

    # Extract features from the formula
    sem_features, struc_features, const_features, var_features = \
        extract_features(dom_tree)

    # Extract inorder and sorted semantic terms
    inorder_sem_terms = generate_inorder_sem_terms(sem_features)
    sorted_sem_terms = generate_sorted_sem_terms(sem_features)

    return inorder_sem_terms, sorted_sem_terms, struc_features, \
           const_features, var_features


def generate_mathmlstr(latex_str):
    """
    Converts latex string to MathML string

    Args:
        latex_str: formula string in latex format.

    Returns:
        A mathml string representation of the formula.

    """
    unescaped_latex = htmlparser.unescape(latex_str)
    mathml_str = l2m.convert(unescaped_latex)
    return mathml_str


def construct_domtree(mathml_str):
    """
    Constructs a DOM tree from MathML string.

    Args:
        mathml_str: MathML string.

    Returns:
        The root of the MathML tree representation.
    """
    root = ET.fromstring(mathml_str)
    return root


def extract_features(dom_tree):
    """
    Extracts semantic, structural, variable, and constant features from a
    DOM tree.

    Args:
        dom_tree: a MathML DOM tree.

    Returns:
        Four iterables corresponding to semantic, structural, variable and
        constant features of a formula.
    """
    sem_features = list()
    struc_features = list()
    cn_features = set()
    var_features = set()
    stack_node = list()

    tf = write_dom_to_tempfile(dom_tree)
    context = ET.iterparse(tf, ['start', 'end'])

    for event, element in context:
        if event == 'start':
            stack_node.append(element.tag)
        else:
            stack_node.pop()

        # converts to UTF-8
        if element.text:
            element_text = htmlparser.unescape(element.text)

        if event == 'start' and element.tag == 'mo':
            sem_features.append(element_text)
            if len(stack_node) > 3:
                struc_features += extract_structural_features(stack_node,
                                                              element)
        elif event == 'start' and element.tag == 'mi' and is_operator_or_function(
                element_text):
            sem_features.append(element_text)
            if len(stack_node) > 3:
                struc_features += extract_structural_features(stack_node,
                                                              element)
        elif element.tag != 'mrow' and element.tag != 'math' and event == \
                'start' and element.findall('.//mi'):
            sem_features.append(element.tag)
            if len(stack_node) > 3:
                struc_features += extract_structural_features(stack_node,
                                                              element)
        elif event == 'start' and element_text != 'e':
            if element.tag == 'mn':
                cn_features.add(
                    extract_structural_features(stack_node, element,
                                                True) + 'cn')
            elif element.tag == 'mi':
                var_features.add(
                    extract_structural_features(stack_node, element, True)
                    + 'var')
    tf.close()

    return sem_features, struc_features, list(cn_features), list(var_features)


def extract_structural_features(stack_node, element, cn_var=False):
    """
    Extract structural features from the node stack.

    Args:
        stack_node: stack of formula features.
        element: current math element tag.
        cn_var: boolean value that indicates the current element is a constant.

    Returns:
        List of structural features.
    """
    nodes = ''

    if cn_var:
        for node in stack_node[2:len(stack_node) - 1]:
            nodes += node + '$'
        return nodes
    else:
        for node in stack_node[2:len(stack_node) - 1]:
            nodes += node + '$'
        if not element.text.strip():
            nodes += element.tag
        else:
            nodes += htmlparser.unescape(element.text)
        return [nodes]


def generate_inorder_sem_terms(sem_features):
    """
    Generates 2, 3, 4-grams of in order semantic terms.

    Args:
        sem_features: list of semantic features.

    Returns:
        List of inorder semantic terms.
    """
    terms = list()

    if len(sem_features) <= 0:
        return terms

    # 4 terms
    terms = [[sem_features[i] + '$' + sem_features[i + 1] + '$' +
              sem_features[i + 2] + '$' + sem_features[i + 3] for i in
              range(len(sem_features) - 3)]]

    # 3 terms
    terms += [[sem_features[i] + '$' + sem_features[i + 1] + '$' +
               sem_features[i + 2] for i in range(len(sem_features) - 2)]]

    # 2 terms
    terms += [[sem_features[i] + '$' + sem_features[i + 1]
               for i in range(len(sem_features) - 1)]]

    return terms


def generate_sorted_sem_terms(sem_features):
    """
    Generates 1, 2, 3, 4-grams of lexicographically sorted semantic terms
    according to UTF-8 order.

    Args:
        sem_features: list of semantic features.

    Returns:
        List of semantic terms in lexicographic order.
    """
    terms = list()

    if len(sem_features) <= 0:
        return terms

    # Sort terms according to UTF-8
    locale.setlocale(locale.LC_ALL, "")
    sem_features.sort(cmp=locale.strcoll)

    # 4 terms
    terms = [[sem_features[i] + '$' + sem_features[i + 1] + '$' +
             sem_features[i + 2] + '$' + sem_features[i + 3]
             for i in range(len(sem_features) - 3)]]

    # 3 terms
    terms += [[sem_features[i] + '$' + sem_features[i + 1] + '$' +
              sem_features[i + 2] for i in range(len(sem_features) - 2)]]

    # 2 terms
    terms += [[sem_features[i] + '$' + sem_features[i + 1]
              for i in range(len(sem_features) - 1)]]

    # 1 term
    terms += [[sem_features[i] for i in range(len(sem_features))]]

    return terms
