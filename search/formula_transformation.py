import math

from meas_models.models import *

import ast
import os
import pickle
import formula_indexer as fi

SCRIPT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(SCRIPT_DIR, "data")
FEATURES_FILE_PATH = os.path.join(DATA_PATH, "formula.feature")
VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.vector")
TFIDF_VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.tfidf.vector")


def transform_formulas(write_vector=False, write_tfidf=False,
                       write_term=False, reindex=False):
    """
    Transforms formula terms into normalized vector representation.

    Args:
        write_vector: Option to write formula term vector into a file or
        overwrite it if it already exists.
        write_tfidf: Option to write normalized formula term tfidf
        vector into a file or overwrite it if it already exists.
        write_term: Option to write all formula terms into a file or
        overwrite it if it already exists.
        reindex: Option to reindex (destroy and recreates) both formula and
        formula index table.
    Returns:
        List of normalized tfidf formula vectors.
    """
    # Generates all terms
    if write_term or not os.path.isfile(FEATURES_FILE_PATH):
        extract_all_distinct_features(reindex)

    with open(FEATURES_FILE_PATH, 'rb') as fp:
        data = pickle.load(fp)
    all_terms = data["all_terms"]

    # Transforms formula to term vector
    if write_vector or not os.path.isfile(VECTOR_FILE_PATH):
        generate_formula_term_vectors(all_terms)

    with open(VECTOR_FILE_PATH, 'rb') as fp:
        formula_term_vectors = pickle.load(fp)

    # Updates term vector with tfidf values then normalize
    N = Formula.objects.count()
    idf_values = compute_idf_values(all_terms, N)
    update_term_vector_tfidf_normalize(formula_term_vectors, all_terms,
                                       idf_values)

    if write_tfidf or not os.path.isfile(TFIDF_VECTOR_FILE_PATH):
        with open(TFIDF_VECTOR_FILE_PATH, 'wb') as fp:
            pickle.dump(formula_term_vectors, fp)
        with open(TFIDF_VECTOR_FILE_PATH + '.txt', 'w') as fp:
            data = str(formula_term_vectors)
            fp.write(data.encode('unicode-escape'))

    return formula_term_vectors


def extract_all_distinct_features(reindex=False):
    """
    Extracts all distinct formula features and writes them into a file.

    Args:
        reindex: Option to reindex (destroy and recreates) both formula and
        formula index table.

    Returns:
        Object containing all the distinct terms sorted lexicographically.
    """
    if reindex: fi.reindex_all_formulas()

    all_formulas = Formula.objects.all()
    total_terms = 0
    formula_term_vector = dict()

    for formula in all_formulas:
        total_terms += update_formula_term_vector(formula,
                                                  formula_term_vector)

    # Distinct terms
    all_terms = formula_term_vector.keys()
    all_terms.sort()

    data = {
        'all_terms': all_terms,
        'total_terms': total_terms,
        'total_distinct_terms': len(all_terms)
    }

    with open(FEATURES_FILE_PATH + '.txt', 'w') as fp:
        data_str = str(data)
        fp.write(data_str.encode('unicode-escape'))

    with open(FEATURES_FILE_PATH, 'wb') as fp:
        pickle.dump(data, fp)

    return data


def update_formula_term_vector(formula, formula_term_freq_map):
    """
    Counts the frequency of all the terms in a formula.

    Args:
        formula: a formula object.
        formula_term_freq_map: mapping between terms and frequency. Term
        frequency is 0 at initial.

    Returns:
        Total terms in a formula.
    """
    total_terms = 0

    if formula.status:
        # 1-gram sorted semantic term
        sorted_temp = ast.literal_eval(formula.sorted_term)
        if sorted_temp:
            formula.sorted_term = sorted_temp[-1]
            total_terms += update_formula_term_counter(formula.sorted_term,
                                                       formula_term_freq_map)
        # structural term
        formula.structure_term = ast.literal_eval(
            formula.structure_term)
        total_terms += update_formula_term_counter(formula.structure_term,
                                                   formula_term_freq_map)
        # constant term
        formula.constant_term = ast.literal_eval(formula.constant_term)
        total_terms += update_formula_term_counter(formula.constant_term,
                                                   formula_term_freq_map)
        # formula term
        formula.variable_term = ast.literal_eval(formula.variable_term)
        total_terms += update_formula_term_counter(formula.variable_term,
                                                   formula_term_freq_map)
    return total_terms


def update_formula_term_counter(terms, formula_term_freq_map):
    """
    Updates the term frequency map of a formula according to its available
    terms.

    Args:
        terms: Available terms of a formula.
        formula_term_freq_map: Mapping between formula term and frequency of a
        formula.

    Returns:
        Total terms updated.
    """
    count = 0

    if terms:
        for term in terms:
            if term in formula_term_freq_map:
                formula_term_freq_map[term] += 1
            else:
                formula_term_freq_map[term] = 1
            count += 1

    return count


def generate_formula_term_vectors(all_terms):
    """
    Generates formula term frequency vectors. Each element in the vector
    corresponds to the term frequency in the formula.

    Args:
        all_terms: List of all distinct terms in sorted order.

    Returns:
        List of formula term frequency vectors.
    """
    all_formulas = Formula.objects.all()
    formula_term_vectors = []

    for formula in all_formulas:
        formula_term_freq_map = {term: 0 for term in all_terms}
        # generate term vector for each formula
        update_formula_term_vector(formula, formula_term_freq_map)
        # sort by keys and convert to list then add to formula_term_vector
        formula_term_vector = [formula_term_freq_map[term] for term in
                               all_terms]
        formula_term_vectors.append(formula_term_vector)

    with open(VECTOR_FILE_PATH + '.txt', 'w') as fp:
        data = str(formula_term_vectors)
        fp.write(data.encode('unicode-escape'))

    with open(VECTOR_FILE_PATH, 'wb') as fp:
        pickle.dump(formula_term_vectors, fp)

    print("Formula term vector model created.")
    return formula_term_vectors


def compute_idf_values(terms, N):
    """
    Maps term to document frequency.

    Args:
        terms: All the sorted distinct formula terms used to compute the IDF
        score.
        N: Total number of formulas.

    Returns:
        Map of a formula term and its IDF value.
    """
    idf_values = dict()

    formula_indexes = FormulaIndex.objects.filter(pk__in=terms)
    for formula_index in formula_indexes:
        idf_values[formula_index.indexkey] = math.log10(
            float(N) / formula_index.df)

    return idf_values


def update_term_vector_tfidf_normalize(formula_term_vectors, all_terms,
                                       idf_values):
    """
    Computes the TFIDF score of a formula vector and normalize its values.

    Args:
        formula_term_vectors: List of formula term vectors.
        all_terms: List of all distinct terms in sorted order.
        idf_values: Map of a formula term and its IDF value.
    """
    # Update with TF-IDF
    for formula_vector in formula_term_vectors:
        for idx_term in range(len(formula_vector)):
            # Term frequency in the formula
            tf = formula_vector[idx_term]
            # Inverse document frequency
            score = 0.0
            if all_terms[idx_term] in idf_values:
                idf = idf_values[all_terms[idx_term]]
                score = tf * idf

            formula_vector[idx_term] = score

    # Normalize vectors
    for formula_vector in formula_term_vectors:
        sqrt_sum_sqr = math.sqrt(sum(map(lambda x: x * x, formula_vector)))
        for idx_term in range(len(formula_vector)):
            if sqrt_sum_sqr != 0:
                formula_vector[idx_term] /= float(sqrt_sum_sqr)

