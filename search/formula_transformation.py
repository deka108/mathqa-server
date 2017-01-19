from collections import Counter
from itertools import chain
from meas_models.models import *

import ast
import math
import os
import pickle
import features_extractor as fe
import formula_indexer as fi

SCRIPT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(SCRIPT_DIR, "data")
FEATURES_FILE_PATH = os.path.join(DATA_PATH, "formula.feature")
VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.vector")
TFIDF_VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.tfidf.vector")


def get_all_terms(write_term=False, reindex=False):
    """
    Generates all the distinct terms from formula features.

    Args:
        reindex: Option to reindex both formula and formula index table.
        write_term: Option to write all terms into a file.

    Returns:
        List of all distinct feature terms in sorted order.
    """
    if write_term or not os.path.isfile(FEATURES_FILE_PATH):
        extract_all_distinct_features(reindex)
    with open(FEATURES_FILE_PATH, 'rb') as fp:
        data = pickle.load(fp)
    return data["all_terms"]


ALL_TERMS = get_all_terms()


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
    all_terms = get_all_terms(write_term, reindex)

    # Transforms formula to term vector
    if write_vector or not os.path.isfile(VECTOR_FILE_PATH):
        generate_formula_term_vectors()

    with open(VECTOR_FILE_PATH, 'rb') as fp:
        formula_term_vectors = pickle.load(fp)

    # Updates term vector with tfidf values then normalize
    N = Formula.objects.count()
    idf_values = compute_idf_values(all_terms, N)
    update_term_vectors_tfidf_normalize(formula_term_vectors, all_terms,
                                        idf_values)

    if write_tfidf or not os.path.isfile(TFIDF_VECTOR_FILE_PATH):
        with open(TFIDF_VECTOR_FILE_PATH, 'wb') as fp:
            pickle.dump(formula_term_vectors, fp)
        with open(TFIDF_VECTOR_FILE_PATH + '.txt', 'w') as fp:
            data = str(formula_term_vectors)
            fp.write(data.encode('unicode-escape'))

    return formula_term_vectors


def read_normalized_tfidf_vector():
    """
    Retrieves normalized tfidf formula feature vectors.

    Returns:
        List of normalized tfidfs formula feature vectors.
    """
    if os.path.isfile(TFIDF_VECTOR_FILE_PATH):
        transform_formulas()

    with open(TFIDF_VECTOR_FILE_PATH, 'rb') as fp:
        normalized_tfidf_vectors = pickle.load(fp)

    return normalized_tfidf_vectors


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
    overall_term_counter = Counter()

    for formula in all_formulas:
        terms = get_terms_from_formula(formula)
        term_counter = Counter(terms)
        overall_term_counter.update(term_counter)

    # Distinct terms
    overall_term_vector = dict(overall_term_counter)
    all_terms = overall_term_vector.keys()
    all_terms.sort()
    total_terms = sum(overall_term_vector.values())

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

    return all_terms


def generate_formula_term_vectors():
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
        formula_term_vector = create_formula_term_vector(formula)
        formula_term_vectors.append(formula_term_vector)

    with open(VECTOR_FILE_PATH + '.txt', 'w') as fp:
        data = str(formula_term_vectors)
        fp.write(data.encode('unicode-escape'))

    with open(VECTOR_FILE_PATH, 'wb') as fp:
        pickle.dump(formula_term_vectors, fp)

    return formula_term_vectors


def create_formula_term_vector(formula):
    """
    Counts the frequency of all the terms in a formula.

    Args:
        formula: a formula object.
        formula_term_freq_map: Maps term to the term frequency. Term
        frequency is 0 at initial.

    Returns:
        Total terms in a formula.
    """
    if formula and formula.status:
        existing_terms = get_terms_from_formula(formula)
        return update_formula_terms_counter(existing_terms)

    return update_formula_terms_counter()


def get_terms_from_formula(formula):
    # 1-gram sorted semantic term
    sorted_temp = ast.literal_eval(formula.sorted_term)
    sorted_term = []
    if sorted_temp: sorted_term = sorted_temp[-1]
    # structural term
    structure_term = ast.literal_eval(formula.structure_term)
    # constant term
    constant_term = ast.literal_eval(formula.constant_term)
    # variable term
    variable_term = ast.literal_eval(formula.variable_term)
    existing_terms = sorted_term + structure_term + constant_term + \
                     variable_term
    return existing_terms


def update_formula_terms_counter(existing_terms):
    all_terms = get_all_terms()
    term_counter_map = dict(Counter(existing_terms))

    formula_term_map = \
        {term:term_counter_map[term] if term in term_counter_map else 0
         for term in all_terms}
    return formula_term_map.values()


def compute_idf_values(terms, N):
    """
    Maps term to idf value of the term.

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


def update_term_vectors_tfidf_normalize(formula_term_vectors, all_terms,
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


def transform_formula(latex_str):
    """
    Transforms latex formula into vector representation of normalized tf idf
    feature scores.

    Args:
        latex_str: Formula in latex format.

    Returns:
        Normalized tfidf vector of the query formula.
    """
    ino_features, sort_features, struc_features, const_features, \
    var_features = fe.generate_features(latex_str)
    sort_features = sort_features[-1]

    formula_term_vector = create_formula_term_vector(sort_features +
                                                     struc_features +
                                                     const_features +
                                                     var_features)

    return formula_term_vector
