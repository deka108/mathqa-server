"""Update and creates an indexed formula table"""
from itertools import chain
from meas_models.models import *

import bisect
import features_extractor as fe
import re

##############   REINDEX START  ##############
# Assumption: database for formulas not satisfied
# Otherwise, removing Formula is not necessary, 
# only updates the new / existing formula
def reindex_all_formulas():
    questions = Question.objects.all()
    
    Formula.objects.all().delete()
    FormulaIndex.objects.all().delete()

    # Reindex formulas in every question 
    for question in Question:
        reindex_formulas_in_question(question.id)


def reindex_formulas_in_question(question_id)
    question = Question.objects.get(id=question_id)
    formulas = extract_formulas_from_question(question_id)

    for formula in formulas:
        new_formula = Formula(content=formula, status=False)
        new_formula.save()
        question.formulas.add(new_formula)

    question.save()

    new_formulas = question.formulas.all()
    
    for formula in new_formulas:
        latex_str = formula.content
        formula_id = formula.id

        mathML = fe.convert_latex2mathml(latex_str)
        create_index_model(mathML, formula_id)


def extract_formulas_from_question(question_id):
    content = Question.objects.get(id=question_id).content

    latex_formulas = []
    bracket_notation = re.compile(r'\\\((.+)\\\)')
    latex_formulas += bracket_notation.findall(content)

    dollar_notation = re.compile(r'\$+(.+)\$+')
    latex_formulas += dollar_notation.findall(content)

    return latex_formulas

#############   REINDEX END    ##############


def create_index_model(mathml, formula_id):
    """
    Update formula table with the extracted formula features
    """
    try:
        formula_obj = get_object_or_404(Formula, pk=formula_id)
        
        if not formula_obj.status:
            #Extract four features of Formula
            (sem_features, struc_features, const_features, var_features) = fe.extract_features(mathml)            
            
            # Generate index terms
            inorder_sem_terms = fe.generate_inorder_sem_terms(sem_features)
            sorted_sem_terms = fe.generate_sorted_sem_terms(sem_features)
            
            #Insert into formula table
            formula_obj.inorder_term = inorder_sem_terms
            formula_obj.sorted_term = sorted_sem_terms
            formula_obj.structure_term = struc_features
            formula_obj.constant_term = const_features
            formula_obj.variable_term = var_features
            formula_obj.status = True
            formula_obj.save()
            
            #Create index term in FormulaIndex table
            for term in chain(inorder_sem_terms, sorted_sem_terms):
                create_formula_index(formula_obj.id, term)
                
            for term in chain(struc_features, const_features, var_features):            
                create_formula_index(formula_obj.id, term)
                                                      
    except (KeyError, Formula.DoesNotExist):
        print "Error"


def create_formula_index(formula_id, term):
    """
    Inverted table that maps the formula term to document ids (formula ids)
    """
    try:
        f_index = FormulaIndex.objects.get(pk=term)
        docsids = re.findall('\d', f_index.docsids)
        formulaid_str = str(formula_id)

        if formulaid_str not in docsids:
            bisect.insort(docsids, formulaid_str)

        f_index.docsids = '#' + '#'.join(docsids) + '#'
        f_index.df = len(docsids)

    except (KeyError, FormulaIndex.DoesNotExist):
        f_index = FormulaIndex(term, '#' + str(formula_id) + '#', 1)
    
    f_index.save()