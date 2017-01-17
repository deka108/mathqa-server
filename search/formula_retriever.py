"""Search tables for formula using the IDF method"""
from itertools import chain

import ast
import features_extractor as fe
import math
import re

from meas_models.models import *




def retrieve_formulas_from_inverted_index(term):
    """

    Args:
        term:

    Returns:

    """
    pass


def retrieve_related_formulas(sorted_sem_terms, k=20):
    related_formulas = set()

    if sorted_sem_terms is None:
        return related_formulas

    for term in sorted_sem_terms:
        try:
            f_index = FormulaIndex.objects.get(pk=term)
            docsids = re.findall('\d+', f_index.docsids)
            docsids = [int(docsid) for docsid in docsids]

            formulas = Formula.objects.filter(pk__in=docsids, status=True)

            # Convert string to list
            for formula in formulas:
                if formula.status:
                    inorder_temp = ast.literal_eval(formula.inorder_term)
                    formula.inorder_term = [term for term in
                                        chain.from_iterable(inorder_temp)]

                    sorted_temp = ast.literal_eval(formula.sorted_term)
                    formula.sorted_term = sorted_temp[len(sorted_temp) - 1]

                    formula.structure_term = ast.literal_eval(
                        formula.structure_term)
                    formula.constant_term = ast.literal_eval(
                        formula.constant_term)
                    formula.variable = ast.literal_eval(
                        formula.variable_term)

                    related_formulas.add(formula)

                if len(related_formulas) >= k:
                    break

            return formulas
        except (KeyError, FormulaIndex.DoesNotExist):
            print("Couldn't find this term in the database.")

    return list(related_formulas)


def sem_matching_score(matching_1gram_sort, unmatching_1gram_sort,
                       matching_ngram_inorder, unmatching_ngram_inorder,
                       IDF_values, N):
    sem_score = 0
    num_of_func = 0

    for term in matching_1gram_sort:
        if term in IDF_values:
            sem_score += IDF_values.get(term)
        if fe.is_function(term):
            num_of_func += 1

    sem_score += num_of_func * math.log10(N)

    for term in unmatching_1gram_sort:
        if term in IDF_values:
            sem_score -= IDF_values.get(term)

    for term in matching_ngram_inorder:
        if term in IDF_values:
            sem_score += IDF_values.get(term)
    return sem_score


def struc_matching_score(matching_struc, IDF_values):
    struc_score = 0
    for term in matching_struc:
        if term in IDF_values:
            struc_score += IDF_values.get(term)

    return struc_score


def cn_matching_score(matching_cn):
    return len(matching_cn)


def var_matching_score(matching_var):
    return len(matching_var)


def compute_IDF_values(query_ino_terms, query_sort_terms, query_struc_fea,
                       related_formulas, N):
    IDF_values = dict()
    terms_collection = set(
        query_ino_terms + query_sort_terms + query_struc_fea)

    for rel_formula in related_formulas:
        terms_collection.update(set(rel_formula.inorder_term +
                                    rel_formula.sorted_term +
                                    rel_formula.structure_term))

    FormulaIndex_obj = FormulaIndex.objects.filter(pk__in=terms_collection)
    for obj in FormulaIndex_obj:
        IDF_values[obj.indexkey] = math.log10(N / obj.df)

    return IDF_values


def compute_score(sem_score_norm, struc_score_norm, cn_score_norm,
                  var_score_norm, a=0.2):
    return ((1 - a) * (sem_score_norm + struc_score_norm) +
            a * (cn_score_norm + var_score_norm)) / 2


def formula_score(query_inoder_ngram, query_sort_1gram, query_struc, query_cn,
                  query_var, retrie_inoder_ngram, retrie_sort_1gram,
                  retrie_struc, retrie_cn, retrie_var, IDF_values, N):
    sem_score = sem_matching_score(
        set(query_sort_1gram) & set(retrie_sort_1gram),
        set(retrie_sort_1gram) - set(query_sort_1gram),
        set(query_inoder_ngram) & set(retrie_inoder_ngram),
        set(retrie_inoder_ngram) - set(query_inoder_ngram),
        IDF_values, N)

    struc_score = struc_matching_score(set(query_struc) & set(retrie_struc),
                                       IDF_values)

    cn_score = cn_matching_score(set(query_cn) & set(retrie_cn))

    var_score = var_matching_score(set(query_var) & set(retrie_var))

    return (sem_score, struc_score, cn_score, var_score)


def formulas_ranking(query_ino_terms, query_sort_1gram, query_struc_fea,
                     query_cn_fea, query_var_fea, related_formulas, IDF_values,
                     N):
    ranked_scores = list()

    (sem_score_norm, struc_score_norm, cn_score_norm, var_score_norm) = \
        formula_score(query_ino_terms, query_sort_1gram, query_struc_fea,
                      query_cn_fea, query_var_fea, query_ino_terms,
                      query_sort_1gram,
                      query_struc_fea, query_cn_fea, query_var_fea, IDF_values,
                      N)

    for rel_formula in related_formulas:
        (sem_score, struc_score, cn_score, var_score) = \
            formula_score(query_ino_terms, query_sort_1gram, query_struc_fea,
                          query_cn_fea, query_var_fea,
                          rel_formula.inorder_term,
                          rel_formula.sorted_term, rel_formula.structure_term,
                          rel_formula.constant_term, rel_formula.variable_term,
                          IDF_values, N)

        if sem_score_norm != 0:
            sem_score = sem_score / sem_score_norm
        if struc_score_norm != 0:
            struc_score = struc_score / struc_score_norm
        if cn_score_norm != 0:
            cn_score = cn_score / cn_score_norm
        if var_score_norm != 0:
            var_score = var_score / var_score_norm
        score = compute_score(sem_score, struc_score, cn_score, var_score)
        if score > 0:
            ranked_scores.append((rel_formula, score))

    results = []
    temp_result = sorted(ranked_scores, key=lambda scores: scores[1],
                         reverse=True)
    for index, (rel_formula, score) in enumerate(temp_result):
        question = rel_formula.question
        results.append(
            [rel_formula.question_id, question.topic_id, question.content,
             rel_formula.formula, index + 1, index + 2, score])

    return results, len(temp_result)


def search_content_formula(latex_str):
    """

    Args:
        latex_str:

    Returns:

    """
    query_ino_terms, query_sort_terms, query_struc_features, \
    query_cn_features, query_var_features = fe.generate_features(latex_str)

    related_formulas = retrieve_related_formulas(query_sort_terms)

    query_ino_terms = [term for term in chain.from_iterable(query_ino_terms)]
    query_sort_terms = query_sort_terms[len(query_sort_terms) - 1]

    N = Formula.objects.count()

    IDF_values = compute_IDF_values(query_ino_terms, query_sort_terms,
                                    query_struc_features, related_formulas, N)

    results, num_of_results = formulas_ranking(query_ino_terms,
                                               query_sort_terms,
                                               query_struc_features,
                                               query_cn_features,
                                               query_var_features,
                                               related_formulas,
                                               IDF_values, N)

    return results, num_of_results
