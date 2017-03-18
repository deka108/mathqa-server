"""Search tables for formula using the IDF method"""
import ast
import math

from itertools import chain
from apiv2.models import Formula, FormulaIndex
from apiv2.search.fsearch import formula_features_extractor as ffe, \
    formula_extractor as fe


def search_formula(latex_str):
    """
    Performs inverted index searching to find questions with the closest
    match with the query.

    Args:
        latex_str: formula string in latex bounded between $$.

    Returns:
        List of questions that has the closest formula match with the query.
    """
    latex_str = fe.extract_latex_from_raw_latex_query(latex_str)
    print("query:")
    print(latex_str)

    # Query feature extraction
    query_ino_terms, query_sort_terms, query_struc_features, \
    query_cn_features, query_var_features = ffe.generate_features(latex_str)

    # Retrieve related formulas
    related_formulas = retrieve_related_formulas(query_sort_terms)

    query_ino_terms = [term for term in chain.from_iterable(query_ino_terms)]
    query_1gram_sort_terms = []

    # 1-gram sorted terms
    if query_sort_terms:
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

    # use the n-gram semantic terms to retrieve relevant formulas
    for term in chain.from_iterable(query_sort_sem_terms):
        try:
            # retrieve from inverted index
            f_index = FormulaIndex.objects.get(pk=term)

            # filter formulas based on formula ids found in inverted index
            formulas = f_index.formulas.all()
            formulas = formulas.filter(status=True)

            # Convert string to list
            for formula in formulas:
                if formula.status:
                    inorder_temp = ast.literal_eval(formula.inorder_term)
                    formula.inorder_term = [term for term in
                                            chain.from_iterable(inorder_temp)]

                    # only 1-gram sorted semantic term is used for formula
                    # ranking
                    sorted_temp = ast.literal_eval(formula.sorted_term)
                    formula.sorted_term = sorted_temp[-1]
                    formula.structure_term = ast.literal_eval(
                        formula.structure_term)
                    formula.constant_term = ast.literal_eval(
                        formula.constant_term)
                    formula.variable_term = ast.literal_eval(
                        formula.variable_term)

                    # union of formulas
                    related_formulas.add(formula)

        except (KeyError, FormulaIndex.DoesNotExist):
            print("Couldn't find this term:%s in the database." % term)

        if len(related_formulas) >= k:
            break

    return list(related_formulas)


def compute_idf_values(query_ino_terms, query_sort_terms, query_struc_features,
                       related_formulas, N):
    """
    Computes the idf values for the query and related formula terms.

    IDF Formula: Math.log10(N / DF(t)), with N as the total number of documents
    (formulas) in the collection and DF as the number of formulas that
    contains the feature term t.

    Args:
        query_ino_terms: List of in-order semantic terms of the query.
        query_sort_terms: List of 1-gram sorted semantic terms of the query.
        query_struc_features: List of the structural features of the query.
        related_formulas: List of related formulas.
        N: Total number of formulas.

    Returns:
        Map of formula term and its IDF value.
    """
    idf_values = dict()
    terms_collection = set(query_ino_terms + query_sort_terms +
                           query_struc_features)

    for rel_formula in related_formulas:
        terms_collection.update(set(rel_formula.inorder_term +
                                    rel_formula.sorted_term +
                                    rel_formula.structure_term))

    formula_indexes = FormulaIndex.objects.filter(pk__in=terms_collection)
    for formula_index in formula_indexes:
        idf_values[formula_index.term_index] = \
            math.log10(float(N) / formula_index.df)

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

    print("Number of formula retrived: %d" % len(scores))
    for (rel_formula, score) in scores:
        print(rel_formula, score)

        if rel_formula.questions.count() > 0:
            results += [{"rel_formula": rel_formula, "question": q} for q in
                    rel_formula.questions.all()]
        else:
            results += [{
                "rel_formula": rel_formula,
                "question": None,
            }]

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

    # normalization denominator
    sem_score_query, struc_score_query, cn_score_query, var_score_query = \
        compute_formula_feature_scores(query_ino_terms, query_sort_1gram,
                                       query_struc_fea, query_cn_fea,
                                       query_var_fea,
                                       query_ino_terms, query_sort_1gram,
                                       query_struc_fea, query_cn_fea,
                                       query_var_fea,
                                       idf_values, N)
    # print("query_sem_score: %s, query_struc_score: %s, query_cn_score: %s, "
    #       "query_var_score: %s" % (str(sem_score_query),
    #                                str(struc_score_query),
    #                                str(cn_score_query),
    #                                str(var_score_query)))

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
        # print("rel_sem_score: %s, rel_struc_score: %s, rel_cn_score: %s, "
        #       "rel_var_score: %s" % (str(sem_score), str(struc_score),
        #                              str(cn_score), str(var_score)))

        # Normalize score
        if sem_score_query != 0:
            sem_score /= float(sem_score_query)
        else:
            sem_score = 0

        if struc_score_query != 0:
            struc_score /= float(struc_score_query)
        else:
            struc_score = 0

        if cn_score_query != 0:
            cn_score /= float(cn_score_query)
        else:
            cn_score = 0

        if var_score_query != 0:
            var_score /= float(var_score_query)
        else:
            var_score = 0

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
            if ffe.is_function(term):
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
                                 cn_score_norm, var_score_norm, a=0.2):
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
