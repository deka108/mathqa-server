from meas_models.models import *
from .features_extractor import * as fe

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
	# content = Questions.objects.get(id=question_id).content

	latex_formulas = []
	bracket_notation = re.compile(r'\\\((.+)\\\)')
	latex_formulas += bracket_notation.findall(content)

	dollar_notation = re.compile(r'\$+(.+)\$+')
	latex_formulas += dollar_notation.findall(content)

	return latex_formulas

#############   REINDEX END    ##############


def insert_posting_list(posting_list, start, end, docid):
    temp = (start+end)/2
    if start == temp:
        if long(posting_list[start]) > docid:
            posting_list.insert(start, docid)
        elif long(posting_list[start]) < docid < long(posting_list[end]):
            posting_list.insert(end,docid)
        elif long(posting_list[end]) < docid:
            posting_list.append(docid)
        else:
            return False
    else:        
        if long(posting_list[temp]) > docid:
            return insert_posting_list(posting_list, start, temp, docid)
        elif long(posting_list[temp]) < docid:
            return insert_posting_list(posting_list, temp, end, docid)
        else:
            return False

    return True


def create_formula_index(indexid, term):
    try:
        f_index = FormulaIndex.objects.get(pk=term)
        posting_list = (f_index.docsids.replace('#', ' ')).split()
        if insert_posting_list(posting_list, 0, len(posting_list)-1, indexid):
            temp = ''
            for item in posting_list:
                temp += '#' + str(item) + '#' 
            f_index.docsids = temp
            f_index.df = len(posting_list)               
    except (KeyError, FormulaIndex.DoesNotExist):
        f_index = FormulaIndex(term, '#'+str(indexid)+'#', 1)
    
    f_index.save()


def create_index_model(mathml, id):
	"""
	Update formula table with the extracted formula features
	"""
    try:
        formula_obj = get_object_or_404(Formula, pk=id)
        
        if formula_obj.status == 0:
            #Extract four types of formula_obj
            (sem_features, struc_features, const_features, var_features) = fe.extract_features(mathml)            
            
            # Generate index terms
            inorder_sem_terms = fe.generate_inorder_sem_terms(sem_features)
            sorted_sem_terms = fe.generate_sorted_sem_terms(sem_features)
            
            #Insert into formulas table
            formula_obj.inorder_term = inorder_sem_terms
            formula_obj.sorted_term = sorted_sem_terms
            formula_obj.structure_term = struc_features
            formula_obj.constant_term = const_features
            formula_obj.variable_term = var_features
            formula_obj.status = 1
            formula_obj.save()
            
            #Create index term in FormulaIndex table
            for term in chain.from_iterable(inorder_sem_terms + sorted_sem_terms):
                create_FormulaIndex(formula_obj.indexid, term)
                
            for term in chain(struc_features, const_features, var_features):            
                create_FormulaIndex(formula_obj.indexid, term)
                                                      
    except (KeyError, Formula.DoesNotExist):
        print "Error"