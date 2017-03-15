"""Update and creates an indexed formula table"""
import bisect
from itertools import chain

import re

import apiv2.search.fsearch.formula_extractor as fe
import apiv2.search.fsearch.formula_features_extractor as ffe
from apiv2.models import Question, Formula, FormulaIndex


def reindex_formulas_in_questions(question_ids):
    """
    Reindex the formula and formula index table.

    Args:
        reset_formula: Option to drop the formula index table and recreates it.
    """
    FormulaIndex.objects.all().delete()

    # Reindex formulas in every question
    for qid in question_ids:
        reindex_formulas_in_question(qid)
        print("Successfully reindex question %s" % qid)

    print("Finished reindexing")


# using latex
def reindex_formulas_in_question(question_id):
    """
    Creates formula and formula index table from a question.

    Args:
        create_formula: Option to to create new formulas from the question.
        question_id: question id
    """
    question = Question.objects.get(id=question_id)

    formulas = fe.extract_formulas_from_text(question.content)

    for formula_str in formulas:
        new_formula = Formula(content=formula_str, status=False,
                              question=question)
        new_formula.save()

    formulas = question.formula_set.all()
    for formula in formulas:
        try:
            create_formula_index_model(formula.id)
        except (KeyError, Formula.DoesNotExist) as e:
            print(e)
            print("Could not create formula index.")


def _get_formula_ids(formulas):
    return [formula.get(u'id') for formula in formulas]


# using pre-defined formulas
def reindex_all_formulas():
    FormulaIndex.objects.all().delete()
    all_formulas = Formula.objects.all()
    print("Formula count: %s" % all_formulas.count())

    # reset status to false
    all_formulas.update(status=False)
    count = 0

    for formula in all_formulas:
        count += create_formula_index_model(formula)

    print("Total formulas reindexed: %d" % count)


def create_formula_index_model(formula_obj):
    """
    Updates formula table with the extracted formula features and creates
    formula index table.

    Args:
        latex_str: formula string in latex format.
        formula_id: formula id.
    """
    try:
        if not formula_obj.status:
            # Extract four features of a Formula
            inorder_sem_terms, sorted_sem_terms, struc_features, \
            const_features, var_features = ffe.generate_features(
                formula_obj.content)

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
                create_update_formula_index(formula_obj, term)

            for term in chain(struc_features, const_features, var_features):
                create_update_formula_index(formula_obj, term)

            print("Reindexed formula: #%d" % formula_obj.id)
            return 1
    except (KeyError, Formula.DoesNotExist) as err:
        print err

    return 0


def create_update_formula_index(formula_obj, term):
    """
    Create an inverted table of formula that maps terms to document ids
    (formula ids), or updates it with the document id if it already exists.

    Args:
        formula_id: formula id.
        term: the formula feature.
    """

    try:
        f_index = FormulaIndex.objects.get(pk=term)
        f_index.formulas.add(formula_obj)

    except (KeyError, FormulaIndex.DoesNotExist):
        f_index = FormulaIndex(term_index=term)
        f_index.save()
        f_index.formulas.add(formula_obj)

    f_index.df = f_index.formulas.all().count()
    f_index.save()