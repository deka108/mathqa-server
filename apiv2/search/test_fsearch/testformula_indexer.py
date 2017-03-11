"""Update and creates an indexed formula table"""
import bisect
from itertools import chain

import re

from apiv2.models import TestFormula, TestFormulaIndex, TestQuestion
from apiv2.search.fsearch import formula_features_extractor as ffe
from apiv2.search.test_fsearch.utils import test_questions_util
from apiv2.search.fsearch import formula_extractor as fe


def reindex_formulas_in_test_questions():
    """
    Reindex the formula and formula index table.

    Args:
        reset_formula: Option to drop the formula index table and recreates it.
    """
    TestFormula.objects.all().delete()
    TestFormulaIndex.objects.all().delete()

    question_ids = test_questions_util.read_test_question_ids()

    # Reindex formulas in every question
    for qid in question_ids:
        reindex_formulas_in_test_question(qid)
        print("Successfully reindex question %s" % qid)

    print("Finished reindexing")


def reindex_formulas_in_test_question(question_id):
    """
    Creates formula and formula index table from a question.

    Args:
        create_formula: Option to to create new formulas from the question.
        question_id: question id
    """
    question = TestQuestion.objects.get(id=question_id)

    formulas = fe.extract_formulas_from_text(question.content)

    for formula_str in formulas:
        new_formula = TestFormula(content=formula_str, status=False,
                                  question=question)
        new_formula.save()

    formulas = question.testformula_set.all()
    for formula in formulas:
        try:
            create_test_formula_index_model(formula.id)
        except (KeyError, TestFormula.DoesNotExist) as e:
            print(e)
            print("Could not create formula index.")


def _get_formula_ids(formulas):
    return [formula.get(u'id') for formula in formulas]


def reindex_test_formulas():
    all_formulas = TestFormula.objects.all()
    print("Formula count: %s" % all_formulas.count())

    # reset status to false
    all_formulas.update(status=False)
    count = 0

    for formula in all_formulas:
        count += create_test_formula_index_model(formula.id)

    print("Total formulas reindexed: %d" % count)


def create_test_formula_index_model(formula_id):
    """
    Updates formula table with the extracted formula features and creates
    formula index table.

    Args:
        latex_str: formula string in latex format.
        formula_id: formula id.
    """
    try:
        formula_obj = TestFormula.objects.get(pk=formula_id)

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

            # Create index term in TestFormulaIndex table
            for term in chain.from_iterable(inorder_sem_terms+sorted_sem_terms):
                create_update_test_formula_index(formula_obj.id, term)

            for term in chain(struc_features, const_features, var_features):
                create_update_test_formula_index(formula_obj.id, term)

            print("Reindexing formula: #%d" % formula_obj.id)
            return 1
    except (KeyError, TestFormula.DoesNotExist) as err:
        print err

    return 0


def create_update_test_formula_index(formula_id, term):
    """
    Create an inverted table of formula that maps terms to document ids
    (formula ids), or updates it with the document id if it already exists.

    Args:
        formula_id: formula id.
        term: the formula feature.
    """

    try:
        f_index = TestFormulaIndex.objects.get(pk=term)
        formulaid_str = str(formula_id)
        docsids = re.findall('\d+', f_index.docsids)

        if formulaid_str not in docsids:
            bisect.insort(docsids, formulaid_str)
            f_index.docsids = '#' + '#'.join(docsids) + '#'
            f_index.df = len(docsids)

    except (KeyError, TestFormulaIndex.DoesNotExist):
        f_index = TestFormulaIndex(term, '#' + str(formula_id) + '#', 1)

    f_index.save()