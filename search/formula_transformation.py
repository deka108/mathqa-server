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


def update_term_vector_tfidf_normalize(all_terms, formula_term_vectors,
                                       idf_values):
    sum_sqr_sqrts = []
    print("=*=Before tfidf:=*=")
    print(formula_term_vectors)
    for vector in formula_term_vectors:
        sum_sqr = 0

        for idx in range(len(vector)):
            tf = vector[idx]
            idf = idf_values[all_terms[idx]]
            score = tf * idf
            vector[idx] = score
            sum_sqr += score ** 2

        sum_sqr_sqrts.append(math.sqrt(sum_sqr))
    print("=*=Before normalization:=*=")
    print(formula_term_vectors)
    for vector in formula_term_vectors:
        for idx in range(len(vector)):
            vector[idx] /= sum_sqr_sqrts[idx]
    print("=*=After normalization:=*=")
    print(formula_term_vectors)


def compute_idf_values(terms, N):
    """

    Args:
        terms:
        N: Total number of formulas.

    Returns:

    """
    idf_values = dict()

    formula_indexes = FormulaIndex.objects.filter(pk__in=terms)
    for formula_index in formula_indexes:
        if formula_index.df != 0:
            idf_values[formula_index.indexkey] = math.log10(N/formula_index.df)

    return idf_values


def transform_formulas(write_tfidf=False, create_vector=False,
                       extract_term=False, reindex=False):
    # generate 1-term per index
    if extract_term or not os.path.isfile(FEATURES_FILE_PATH):
        extract_all_distinct_features(reindex)

    with open(FEATURES_FILE_PATH, 'rb') as fp:
        data = pickle.load(fp)
    all_terms = data["all_terms"]

    # transform formula to term vector
    if create_vector or not os.path.isfile(VECTOR_FILE_PATH):
        create_formula_term_vector_model(all_terms)
    with open(VECTOR_FILE_PATH, 'rb') as fp:
        formula_term_vectors = pickle.load(fp)

    # update term vector with tfidf values and normalize
    N = Formula.objects.count()
    idf_values = compute_idf_values(all_terms, N)
    update_term_vector_tfidf_normalize(all_terms, formula_term_vectors,
                                       idf_values)

    if write_tfidf or not os.path.isfile(TFIDF_VECTOR_FILE_PATH):
        with open(TFIDF_VECTOR_FILE_PATH, 'wb') as fp:
            pickle.dump(formula_term_vectors, fp)
        with open(TFIDF_VECTOR_FILE_PATH + '.txt', 'w') as fp:
            data = str(formula_term_vectors)
            fp.write(data.encode('unicode-escape'))
    
    return formula_term_vectors


def extract_all_distinct_features(reindex=False):
    if reindex: fi.reindex_all_formulas()

    all_formulas = Formula.objects.all()
    total_terms = 0
    formula_term_vector = dict()

    for formula in all_formulas:
        total_terms += extract_formula_term_vector(formula,
                                                   formula_term_vector)

    all_terms = formula_term_vector.keys()
    all_terms.sort()

    data = {
        'all_terms': all_terms,
        'total_terms': total_terms,
        'distinct_terms': len(all_terms)
    }

    with open(FEATURES_FILE_PATH + '.txt', 'w') as fp:
        data_str = str(data)
        fp.write(data_str.encode('unicode-escape'))

    with open(FEATURES_FILE_PATH, 'wb') as fp:
        pickle.dump(data, fp)

    return data


def extract_formula_term_vector(formula, formula_term_vector):
    total_terms = 0

    if formula.status:
        # 1-gram sorted semantic term
        sorted_temp = ast.literal_eval(formula.sorted_term)
        if sorted_temp:
            formula.sorted_term = sorted_temp[-1]
            total_terms += update_formula_term_counter(formula.sorted_term,
                                                       formula_term_vector)
        # structural term
        formula.structure_term = ast.literal_eval(
            formula.structure_term)
        total_terms += update_formula_term_counter(formula.structure_term,
                                                   formula_term_vector)
        # constant term
        formula.constant_term = ast.literal_eval(formula.constant_term)
        total_terms += update_formula_term_counter(formula.constant_term,
                                                   formula_term_vector)
        # formula term
        formula.variable_term = ast.literal_eval(
            formula.variable_term)
        total_terms += update_formula_term_counter(formula.constant_term,
                                                   formula_term_vector)
    return total_terms


def update_formula_term_counter(formulas, formula_term_vector):
    count = 0

    if formulas:
        for term in formulas:
            if term in formula_term_vector:
                formula_term_vector[term] += 1
            else:
                formula_term_vector[term] = 1
            count += 1

    return count


def create_formula_term_vector_model(all_terms):
    all_formulas = Formula.objects.all()

    formula_term_vectors = []

    for formula in all_formulas:
        formula_term_vector_map = {term:0 for term in all_terms}

        # generate term vector for each formula
        extract_formula_term_vector(formula, formula_term_vector_map)

        # sort by keys and convert to list add to formula_term_vector
        sorted_terms = formula_term_vector_map.keys()
        sorted_terms.sort()

        formula_term_vector = [formula_term_vector_map[term] for term in
                               sorted_terms]
        formula_term_vectors.append(formula_term_vector)

    with open(VECTOR_FILE_PATH + '.txt', 'w') as fp:
        data = str(formula_term_vectors)
        fp.write(data.encode('unicode-escape'))

    with open(VECTOR_FILE_PATH, 'wb') as fp:
        pickle.dump(data, fp)

    return formula_term_vectors
