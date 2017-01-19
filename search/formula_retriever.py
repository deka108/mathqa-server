"""Search tables for formula using the IDF method"""
from itertools import chain
from meas_models.models import *

import ast
import features_extractor as fe
import math
import re


def search_formula(latex_str):
    """
    Performs inverted index searching to find questions with the closest
    match with the query.

    Args:
        latex_str: formula string in latex format.

    Returns:
        List of questions that has the closest formula match with the query.
    """
    # Query feature extraction
    query_ino_terms, query_sort_terms, query_struc_features, \
    query_cn_features, query_var_features = fe.generate_features(latex_str)

    # Retrieve related formulas
    related_formulas = retrieve_related_formulas(query_sort_terms)

    query_ino_terms = [term for term in chain.from_iterable(query_ino_terms)]
    # 1-gram sorted terms
    query_1gram_sort_terms = query_sort_terms[-1]

    N = Formula.objects.count()

    # Compute idf values
    idf_values = compute_idf_values(query_ino_terms, query_1gram_sort_terms,
                                    query_struc_features, related_formulas, N)

    # Rank formula result
    results = rank_formula_result(query_ino_terms, query_1gram_sort_terms,
                                  query_struc_features, query_cn_features,
                                  query_var_features, related_formulas,
                                  idf_values, N)
    return results


def retrieve_related_formulas(query_sort_sem_terms, k=20):
    """
    Retrieves related formulas of thq query.

    Args:
        query_sort_sem_terms: List of sorted terms of the query.
        k: Number of related formulas.

    Returns:
        List of related formulas.
    """
    related_formulas = set()

    if query_sort_sem_terms is None:
        return related_formulas

    for term in chain.from_iterable(query_sort_sem_terms):
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

                    # 1-gram sorted semantic term
                    sorted_temp = ast.literal_eval(formula.sorted_term)
                    formula.sorted_term = sorted_temp[-1]
                    formula.structure_term = ast.literal_eval(
                        formula.structure_term)
                    formula.constant_term = ast.literal_eval(
                        formula.constant_term)
                    formula.variable_term = ast.literal_eval(
                        formula.variable_term)

                    related_formulas.add(formula)

                if len(related_formulas) >= k:
                    break

        except (KeyError, FormulaIndex.DoesNotExist):
            print("Couldn't find this term:%s in the database." % term)

    return list(related_formulas)


def compute_idf_values(query_ino_terms, query_sort_terms, query_struc_fea,
                       related_formulas, N):
    """
    Computes the idf values for the query and related formula terms.

    IDF Formula: Math.log10(N / DF(t)), with N as the total number of documents
    (formulas) in the collection and DF as the number of formulas that
    contains the feature term t.

    Args:
        query_ino_terms: List of in-order semantic terms of the query.
        query_sort_terms: List of 1-gram sorted semantic terms of the query.
        query_struc_fea: List of the structural features of the query.
        related_formulas: List of related formulas.
        N: Total number of formulas.

    Returns:
        Map of formula term and its IDF value.
    """
    idf_values = dict()
    terms_collection = set(query_ino_terms + query_sort_terms +
                           query_struc_fea)

    for rel_formula in related_formulas:
        terms_collection.update(set(rel_formula.inorder_term +
                                    rel_formula.sorted_term +
                                    rel_formula.structure_term))

    formula_indexes = FormulaIndex.objects.filter(pk__in=terms_collection)
    for formula_index in formula_indexes:
        if formula_index.df != 0:
            idf_values[formula_index.indexkey] = \
                math.log10(float(N)/formula_index.df)

    return idf_values


def rank_formula_result(query_ino_terms, query_sort_1gram, query_struc_fea,
                        query_cn_fea, query_var_fea, related_formulas,
                        idf_values, N):
    """
    Rank the query result according to the matching score in descending order.

    Args:
        query_ino_terms: List of in-order semantic terms of the query.
        query_sort_1gram: List of 1-gram sorted semantic terms of the query.
        query_struc_fea: List of the structural features of the query.
        query_cn_fea: List of the constant features of the query.
        query_var_fea: List of the variable features of the query.
        related_formulas: List of related formulas.
        idf_values: Map of formula term and its IDF score.
        N: Total number of formulas.

    Returns:
        List of question ids sorted according to their formula matching score.
    """
    scores = compute_formula_scores(query_ino_terms, query_sort_1gram,
                                    query_struc_fea, query_cn_fea,
                                    query_var_fea, related_formulas,
                                    idf_values, N)

    scores.sort(key=lambda x: x[1], reverse=True)

    results = []

    for (rel_formula, score) in scores:
        question = rel_formula.question
        if question not in results:
            results.append(question)

    return results


def compute_formula_scores(query_ino_terms, query_sort_1gram, query_struc_fea,
                           query_cn_fea, query_var_fea, related_formulas,
                           idf_values, N):
    """
    Computes the total formula scores of the related formulas.

    Args:
        query_ino_terms: List of in-order semantic terms of the query.
        query_sort_1gram: List of 1-gram sorted semantic terms of the query.
        query_struc_fea: List of the structural features of the query.
        query_cn_fea: List of the constant features of the query.
        query_var_fea: List of the variable features of the query.
        related_formulas: List of related formulas.
        idf_values: Map of formula term and its IDF score.
        N: Total number of formulas.

    Returns:
        List of tuples containing the related formula and its matching score.
    """
    scores = list()
    sem_score_query, struc_score_query, cn_score_query, var_score_query = \
        compute_formula_feature_scores(query_ino_terms, query_sort_1gram,
                                       query_struc_fea, query_cn_fea,
                                       query_var_fea,
                                       query_ino_terms, query_sort_1gram,
                                       query_struc_fea, query_cn_fea,
                                       query_var_fea,
                                       idf_values, N)
    for rel_formula in related_formulas:
        sem_score, struc_score, cn_score, var_score = \
            compute_formula_feature_scores(query_ino_terms, query_sort_1gram,
                                           query_struc_fea, query_cn_fea,
                                           query_var_fea,
                                           rel_formula.inorder_term,
                                           rel_formula.sorted_term,
                                           rel_formula.structure_term,
                                           rel_formula.constant_term,
                                           rel_formula.variable_term,
                                           idf_values, N)

        # Normalize score
        if sem_score_query != 0:
            sem_score /= float(sem_score_query)
        if struc_score_query != 0:
            struc_score /= float(struc_score_query)
        if cn_score_query != 0:
            cn_score /= float(cn_score_query)
        if var_score_query != 0:
            var_score /= float(var_score_query)
        score = compute_total_matching_score(sem_score, struc_score, cn_score,
                                             var_score)

        if score > 0:
            scores.append((rel_formula, score))
    return scores


def compute_formula_feature_scores(query_ino_ngram, query_sort_1gram,
                                   query_struc, query_cn, query_var,
                                   rel_ino_ngram, rel_sort_1gram,
                                   rel_struc, rel_cn, rel_var,
                                   idf_values, N):
    """
    Computes the feature matching score between query and a related formula.

    Args:
        query_ino_ngram: List of in-order semantic terms of the query.
        query_sort_1gram: List of 1-gram sorted semantic terms of the query.
        query_struc: List of the structural features of the query.
        query_cn: List of the constant features of the query.
        query_var: List of the variable features of the query.
        rel_ino_ngram: List of in-order semantic terms of the related formula.
        rel_sort_1gram: List of 1-gram sorted semantic terms of the related
        formula.
        rel_struc: List of the structural features of the related formula.
        rel_cn: List of the constant features of the related formula.
        rel_var: List of the variable features of the related formula.
        idf_values: Map of formula term and its IDF score.
        N: Total number of formulas.

    Returns:
        Semantic feature matching score, structural matching feature score,
        constant feature matching score and variable matching feature score.
    """
    # Semantic matching score
    sem_score = compute_sem_matching_score(
        set(query_sort_1gram) & set(rel_sort_1gram),
        set(rel_sort_1gram) ^ set(query_sort_1gram),
        set(query_ino_ngram) & set(rel_ino_ngram),
        idf_values, N)
    # Structural matching score
    struc_score = compute_struc_matching_score(
        set(query_struc) & set(rel_struc), idf_values)
    # Constant matching score
    cn_score = compute_cn_matching_score(set(query_cn) & set(rel_cn))
    # Variable matching score
    var_score = compute_var_matching_score(set(query_var) & set(rel_var))

    return sem_score, struc_score, cn_score, var_score


def compute_sem_matching_score(matched_sort_1gram, unmatched_sort_1gram,
                               matched_ino_ngram, idf_values, N):
    """
    Computes the semantic features matching score.

    Args:
        matched_sort_1gram: Set of 1-gram sorted semantic terms that exists
        in both query and related formula.
        unmatched_sort_1gram: Set of 1-gram semantic sorted terms that does
        not exist in both query and related formula.
        matched_ino_ngram: Set of in-order semantic terms that exists in
        both query and related formula.
        idf_values: Map of formula term and its IDF score.
        N: Total number of formulas.

    Returns:
        The semantic matching score.
    """
    sem_score = 0
    num_of_func = 0

    for term in matched_sort_1gram:
        if term in idf_values:
            sem_score += idf_values.get(term)

            # if the matching terms is a function
            if fe.is_function(term):
                num_of_func += 1

    sem_score += num_of_func * math.log10(N)

    for term in unmatched_sort_1gram:
        if term in idf_values:
            sem_score -= idf_values.get(term)

    for term in matched_ino_ngram:
        if term in idf_values:
            sem_score += idf_values.get(term)

    return sem_score


def compute_struc_matching_score(matching_struc, idf_values):
    """
    Computes the structural matching score.

    Args:
        matching_struc: Set of structural features that exists in both query
        and related formula.
        idf_values: Map of formula term and its IDF score.

    Returns:
        The structural matching score.
    """
    struc_score = 0
    for term in matching_struc:
        if term in idf_values:
            struc_score += idf_values.get(term)

    return struc_score


def compute_cn_matching_score(matching_cn):
    """
    Computes the constant features matching score.

    Args:
        matching_cn: Set of constant features that exists in both query and
        related formula.

    Returns:
        The constant matching score.
    """
    return len(matching_cn)


def compute_var_matching_score(matching_var):
    """
    Computes the variable features matching score.

    Args:
        matching_var: list of matching variable terms.

    Returns:
        The variable matching sco
    """
    return len(matching_var)


def compute_total_matching_score(sem_score_norm, struc_score_norm,
                                 cn_score_norm, var_score_norm, a=0.1):
    """
    Computes overall formula features score.

    It discriminates the contributions between features. Semantic and
    structural features are more important than constant and variable
    features and thus given more weights.

    Args:
        sem_score_norm: Normalized semantic matching score.
        struc_score_norm: Normalized structural matching score.
        cn_score_norm: Normalized constant matching score.
        var_score_norm: Normalized variable matching score.
        a: weight the contribution between features.

    Returns:
        The total formula matching score.
    """
    return ((1 - a) * (sem_score_norm + struc_score_norm) +
            a * (cn_score_norm + var_score_norm)) / float(2)
