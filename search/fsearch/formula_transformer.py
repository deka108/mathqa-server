from collections import Counter
from meas_models.models import *

import ast
import math
import os
import pickle
import features_extractor as fe
import formula_indexer as fi

SCRIPT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(SCRIPT_DIR, "../data")
FEATURES_FILE_PATH = os.path.join(DATA_PATH, "formula.feature")
TERM_TFIDF_FILE_PATH = os.path.join(DATA_PATH, "formula.term.tfidf")
TFIDF_VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.tfidf.vector")
VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.vector")


def transform_formulas(write_vector=False, write_tfidf=False):
    """
    Transforms formula terms into normalized vector representation.

    Args:
        write_vector: Option to write formula term vector into a file or
        overwrite it if it already exists.
        write_tfidf: Option to write normalized formula term tfidf
        vector into a file or overwrite it if it already exists.
    Returns:
        List of normalized tfidf formula vectors.
    """
    # Transforms formula to term vector
    if write_vector or not os.path.isfile(VECTOR_FILE_PATH):
        generate_formula_term_vectors()

    with open(VECTOR_FILE_PATH, 'rb') as fp:
        formula_term_vectors = pickle.load(fp)

    update_term_vectors_tfidf_normalize(formula_term_vectors)

    if write_tfidf or not os.path.isfile(TFIDF_VECTOR_FILE_PATH):
        with open(TFIDF_VECTOR_FILE_PATH, 'wb') as fp:
            pickle.dump(formula_term_vectors, fp)
        with open(TFIDF_VECTOR_FILE_PATH + '.txt', 'w') as fp:
            data = str(formula_term_vectors)
            fp.write(data.encode('unicode-escape'))

    return formula_term_vectors


def generate_formula_term_vectors():
    """
    Generates formula term frequency vectors. Each element in the vector
    corresponds to the term frequency of a formula.

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
    Generates the formula term frequency vector from a formula.

    Args:
        formula: a formula object.

    Returns:
        List of term frequencies of a formula.
    """
    if formula and formula.status:
        existing_terms = get_terms_from_formula(formula)
        return create_term_vector(existing_terms)

    return create_term_vector()


def get_terms_from_formula(formula):
    """
    Generate all the terms in a formula.

    Args:
        formula: a formula object.

    Returns:
        List of formula terms.
    """
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


def create_term_vector(existing_terms):
    """
    Generates the formula term frequency vector from list of terms.

    Args:
        existing_terms: List of terms that exists in a formula.

    Returns:
        List of term frequencies of a formula.
    """
    all_terms = get_all_terms()
    term_counter_map = dict(Counter(existing_terms))

    formula_term_map = {term: term_counter_map[term]
    if term in term_counter_map else 0 for term in all_terms}

    return formula_term_map.values()


def get_all_terms(write_term=False, reindex=False):
    """
    Generates all the distinct terms from all formulas.

    Args:
        write_term: Option to write all the distinct terms into a file.
        reindex: Option to reindex (destroy and recreates) the formula table.

    Returns:
        List of all distinct feature terms in sorted order.
    """
    if write_term or not os.path.isfile(FEATURES_FILE_PATH):
        return extract_all_distinct_features(reindex)
    with open(FEATURES_FILE_PATH, 'rb') as fp:
        data = pickle.load(fp)
    return data["all_terms"]


def extract_all_distinct_features(reindex=False):
    """
    Extracts all distinct formula features and writes them into a file.

    Args:
        reindex: Option to reindex (destroy and recreates) the formula table.

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
    overall_term_map = dict(overall_term_counter)
    all_terms = overall_term_map.keys()
    all_terms.sort()
    total_terms = sum(overall_term_map.values())

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


def update_term_vectors_tfidf_normalize(term_vectors):
    """
    Computes the TFIDF score of list of term vectors and normalize their
    values.

    Args:
        term_vectors: List of formula term vectors.
    """
    all_terms = get_all_terms()
    idf_values = get_idf_values()
    # Update with TF-IDF
    for term_vector in term_vectors:
        update_term_vector_tfidf_score(term_vector, all_terms, idf_values)
    # Normalize vectors
    for term_vector in term_vectors:
        update_term_vector_normalize(term_vector)


def get_idf_values(write_idf=False):
    """
    Generates list of the idf score of all terms.

    Args:
        write_idf: Option to write idf values object into a file.

    Returns:
        Map of a formula term to its IDF score.
    """
    if write_idf or not os.path.isfile(TERM_TFIDF_FILE_PATH):
        return compute_idf_values()
    with open(TERM_TFIDF_FILE_PATH, 'rb') as fp:
        idf_values = pickle.load(fp)
    return idf_values


def compute_idf_values():
    """
    Maps term to idf value of the term.

    Returns:
        Map of a formula term and its IDF value.
    """
    all_terms = get_all_terms()
    N = Formula.objects.count()
    formula_indexes = FormulaIndex.objects.filter(pk__in=all_terms)
    idf_values = dict()

    for formula_index in formula_indexes:
        idf_values[formula_index.indexkey] = \
            math.log10(float(N) / formula_index.df)

    with open(TERM_TFIDF_FILE_PATH + '.txt', 'w') as fp:
        data = str(idf_values)
        fp.write(data.encode('unicode-escape'))
    with open(TERM_TFIDF_FILE_PATH, 'wb') as fp:
        pickle.dump(idf_values, fp)

    return idf_values


def update_term_vector_normalize(term_vector):
    """
    Normalizes a term vector.

    Args:
        term_vector: List of term frequencies of a formula.
    """
    sqrt_sum_sqr = math.sqrt(sum(map(lambda x: x * x, term_vector)))
    for idx_term in range(len(term_vector)):
        if sqrt_sum_sqr != 0:
            term_vector[idx_term] /= float(sqrt_sum_sqr)


def update_term_vector_tfidf_score(term_vector, all_terms, idf_values):
    """
    Computes the tfidf score of a term vector.

    Args:
        term_vector: List of
        all_terms: List of all distinct feature terms in sorted order.
        idf_values: Map of a formula term to its IDF score.
    """
    for idx_term in range(len(term_vector)):
        # Term frequency in the formula
        tf = term_vector[idx_term]
        # Inverse document frequency
        score = 0.0
        term = all_terms[idx_term]
        if term in idf_values:
            idf = idf_values[term]
            score = tf * idf

        term_vector[idx_term] = score


def read_normalized_tfidf_vectors():
    """
    Retrieves normalized tfidf formula feature vectors.

    Returns:
        List of normalized tfidfs formula feature vectors.
    """
    if not os.path.isfile(TFIDF_VECTOR_FILE_PATH):
        return transform_formulas()

    with open(TFIDF_VECTOR_FILE_PATH, 'rb') as fp:
        normalized_tfidf_vectors = pickle.load(fp)

    return normalized_tfidf_vectors
        

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
    all_terms = get_all_terms()
    idf_values = get_idf_values()

    update_term_vector_tfidf_score(formula_term_vector, all_terms, idf_values)
    update_term_vector_normalize(formula_term_vector)

    return formula_term_vector
