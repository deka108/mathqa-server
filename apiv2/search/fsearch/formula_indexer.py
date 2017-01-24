"""Update and creates an indexed formula table"""
from itertools import chain
from meas_models.models import *

import bisect
import features_extractor as fe
import re


def reindex_all_formulas(reset_formula=False):
    """
    Reindex the formula and formula index table.

    Args:
        reset_formula: Option to drop the formula index table and recreates it.
    """
    questions = Question.objects.all()

    if reset_formula:
        Formula.objects.all().delete()
    else:
        Formula.objects.all().update(status=False)

    FormulaIndex.objects.all().delete()

    # Reindex formulas in every question 
    for question in questions:
        reindex_formulas_in_question(question.id, reset_formula)


def reindex_formulas_in_question(question_id, create_formula=False):
    """
    Creates formula and formula index table from a question.

    Args:
        create_formula: Option to to create new formulas from the question.
        question_id: question id
    """
    question = Question.objects.get(id=question_id)

    if create_formula:
        formulas = extract_formulas_from_question(question_id)

        for formula_str in formulas:
            new_formula = Formula(content=formula_str, status=False,
                                  question=question)
            new_formula.save()

    formulas = question.formula_set.all()
    for formula in formulas:
        try:
            create_formula_index_model(formula.content, formula.id)
        except (KeyError, Formula.DoesNotExist) as e:
            print(e)
            print("Could not create formula index.")


def extract_formulas_from_question(question_id):
    """
    Extract latex formulas from a question.

    Args:
        question_id: question id.

    Returns:
        List of latex formulas.
    """
    content = Question.objects.get(id=question_id).content

    latex_formulas = []
    dollar_notation = re.compile(r'\$+([^\$]+)\$+')
    latex_formulas += dollar_notation.findall(content)

    bracket_notation = re.compile(r'\\\(([^$]+)\\\)')
    latex_formulas += bracket_notation.findall(content)

    return set(latex_formulas)


def create_formula_index_model(latex_str, formula_id):
    """
    Updates formula table with the extracted formula features and creates
    formula index table.

    Args:
        latex_str: formula string in latex format.
        formula_id: formula id.
    """
    try:
        formula_obj = Formula.objects.get(pk=formula_id)

        if not formula_obj.status:
            # Extract four features of a Formula
            inorder_sem_terms, sorted_sem_terms, struc_features, \
            const_features, var_features = fe.generate_features(latex_str)

            # Insert features into formula table
            formula_obj.inorder_term = inorder_sem_terms
            formula_obj.sorted_term = sorted_sem_terms
            formula_obj.structure_term = struc_features
            formula_obj.constant_term = const_features
            formula_obj.variable_term = var_features
            formula_obj.status = True
            formula_obj.save()

            # Create index term in FormulaIndex table
            for term in chain.from_iterable(inorder_sem_terms+sorted_sem_terms):
                create_update_formula_index(formula_obj.id, term)

            for term in chain(struc_features, const_features, var_features):
                create_update_formula_index(formula_obj.id, term)

    except (KeyError, Formula.DoesNotExist) as err:
        print err


def create_update_formula_index(formula_id, term):
    """
    Create an inverted table of formula that maps terms to document ids
    (formula ids), or updates it with the document id if it already exists.

    Args:
        formula_id: formula id.
        term: the formula feature.
    """

    try:
        f_index = FormulaIndex.objects.get(pk=term)
        formulaid_str = str(formula_id)
        docsids = re.findall('\d+', f_index.docsids)

        if formulaid_str not in docsids:
            bisect.insort(docsids, formulaid_str)
            f_index.docsids = '#' + '#'.join(docsids) + '#'
            f_index.df = len(docsids)

    except (KeyError, FormulaIndex.DoesNotExist):
        f_index = FormulaIndex(term, '#' + str(formula_id) + '#', 1)

    f_index.save()