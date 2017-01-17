"""Extract features from Formula"""
from tempfile import TemporaryFile

import xml.etree.ElementTree as ET
import HTMLParser
import latex2mathml.converter as l2m
import locale


htmlparser = HTMLParser.HTMLParser()


def write_dom_to_tempfile(root):
    """
    Writes XML into a temporary file
    """
    # tree = ET.ElementTree(root)
    # tmp = TemporaryFile(suffix=".xml")
    # tree.write(tmp)
    # tmp.seek(0)
    # return tmp
    for e in list(root[0]):
        root.append(e)     
    del root[0]
    
    tree = ET.ElementTree(root)
    tempfile = TemporaryFile(suffix='.xml')
    tree.write(tempfile)
    tempfile.seek(0)
    return tempfile


def print_dom_tree(domtree):
    """
    Debugging purposes
    """
    for elt in domtree.iter(): 
        print("%s: '%s'" % (elt.tag, elt.text))


def is_function(term):
    """
    List of mathematical functions
    """
    operator_terms = ('lim', 'Lim', 'sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh',
                      'cot', 'sec', 'cosec', 'csc', 'log', 'ln', 'lg', 'det', 'gcd',
                      'lcm', 'min', 'max', 'sqrt', 'root', 'frac', 'sub', 'sup',
                      'under', 'alpha', 'beta', 'gamma', 'times', 'neg')
    greek_letters = ('alpha', 'beta', 'gamma', 'delta' ,'epsilon', 'theta', 'Theta',
        '')
    return term.endswith(operator_terms) or term == 'e'


def generate_features(latex_str):
    """
    Converts latex string into MathML string, convert MathML string into a DOM tree,'
    and generate four formula features
    """
    mathml_str = convert_latex2mathml(latex_str)
    dom_tree = construct_domtree(mathml_str)
    return extract_features(dom_tree)


def convert_latex2mathml(latex_str):
    """
    Converts latex string to MathML string
    """
    return l2m.convert(latex_str)


def construct_domtree(mathml_str):
    """
    Constructs DOM tree from MathML string
    """
    root = ET.fromstring(mathml_str)
    return root


def extract_features(dom_tree):
    """
    Extracts semantic, structural, variable, and constant features from a DOM tree
    """
    sem_features = list()
    struc_features = list()
    cn_features = set()
    var_features = set()
    stack_node = list()

    et = write_dom_to_tempfile(dom_tree)
    context = ET.iterparse(et, ['start', 'end'])

    for event, element in context:
        if event == 'start':
            stack_node.append(element.tag)
        else:
            stack_node.pop()

        if element.text:
            element_text = htmlparser.unescape(element.text)

        if event == 'start' and element.tag == 'mo':
            sem_features.append(element_text)
            if len(stack_node) > 2:
                struc_features += extract_structural_features(stack_node, element)
        elif event == 'start' and element.tag == 'mi' and is_function(element_text):
            sem_features.append(element_text)
            if len(stack_node) > 2:
                struc_features += extract_structural_features(stack_node, element)
        elif element.tag != 'mrow' and element.tag != 'math' and \
                event == 'start' and element.find('.//mi'):
            sem_features.append(element.tag)
            if len(stack_node) > 2:
                struc_features += extract_structural_features(stack_node, element)
        elif event == 'start' and element_text != 'e':
            if element.tag == 'mn':
                cn_features.add(extract_structural_features(stack_node, element, True) + 'cn')
            elif element.tag == 'mi':
                var_features.add(extract_structural_features(stack_node, element, True)
                                      + 'var')
    et.close()

    return (sem_features, struc_features, list(cn_features), list(var_features))


def extract_structural_features(stack_node, element, cn_var=False):
    """
    Extract structural features
    """
    nodes = ''

    if cn_var:
        for node in stack_node[1:len(stack_node)-1]:
            nodes += node + '$'
        return nodes
    else:
        for node in stack_node[1:len(stack_node)-1]:
            nodes += node + '$'
        if not element.text:
            nodes += element.tag
        else:
            nodes += htmlparser.unescape(element.text)
        return [nodes]


def generate_inorder_sem_terms(sem_features):
    """
    Generates 2, 3, 4-grams of ordered semantic terms
    """
    terms = list()

    if len(sem_features) <= 0:
        return terms

    # 4 terms
    terms = [[sem_features[i] + '$' + sem_features[i + 1] + '$' + sem_features[i + 2]
              + '$' + sem_features[i + 3] for i in range(len(sem_features) - 3)]]

    # 3 terms
    terms += [[sem_features[i] + '$' + sem_features[i + 1] + '$' + sem_features[i + 2]
               for i in range(len(sem_features)-2)]]

    # 2 terms
    terms += [[sem_features[i] + '$' + sem_features[i + 1]
               for i in range(len(sem_features) - 1)]]

    return terms


def generate_sorted_sem_terms(sem_features):
    """
    Generates 1, 2, 3, 4-grams of lexigraphically sorted semantic terms
    """
    terms = list()

    if len(sem_features) <= 0:
        return terms

    # Sort terms according to UTF-8
    locale.setlocale(locale.LC_ALL, "")
    sem_features.sort(cmp=locale.strcoll)

    # 4 terms
    terms = [[sem_features[i] + '$' + sem_features[i+1] + '$' + sem_features[i+2]
              + '$' + sem_features[i+3] for i in range(len(sem_features)-3)]]

    # 3 terms
    terms += [[sem_features[i] + '$' + sem_features[i+1] + '$'
               + sem_features[i+2] for i in range(len(sem_features)-2)]]

    # 2 terms
    terms += [[sem_features[i] + '$' + sem_features[i+1]
               for i in range(len(sem_features)-1)]]

    # 1 term
    terms += [[sem_features[i] for i in range(len(sem_features))]]
    
    return terms
