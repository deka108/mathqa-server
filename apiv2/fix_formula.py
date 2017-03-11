import HTMLParser
import json

import apiv2.search.fsearch.formula_extractor
import latex2mathml.converter as lml
import re

import apiv2.search.fsearch.formula_features_extractor
from apiv2.search.fsearch import formula_features_extractor as fe
from .models import *

INT_NOTATION = re.compile(r'\\int\^.+')
h = HTMLParser.HTMLParser()


def print_mml(latex_str): print(h.unescape(lml.convert(latex_str)))


def check_question_content():
    questions = Question.objects.all()
    broken = []

    for question in questions:
        formulastrs = apiv2.search.utils.formula_extractor.extract_formulas_from_text(question.content)

        try:
            for formulastr in formulastrs:
                try:
                    fe.generate_features(formulastr)
                except Exception as e:
                    err_obj = {"id": question.id, "formula": formulastr,
                               "error": str(e)}
                    broken.append(err_obj)
                    print(err_obj)
        except Exception as e:
            err_obj = {"id": question.id, "question_content": question.content,
                       "error": str(e)}
            broken.append(err_obj)
            print(err_obj)

    with open('question_errors.json', 'w') as fp:
        json.dump(broken, fp, indent=2)

    return broken


def check_keypoint_content():
    keypoints = KeyPoint.objects.all()
    broken = []

    for keypoint in keypoints:
        formulastrs = apiv2.search.utils.formula_extractor.extract_formulas_from_text(keypoint.content)

        try:
            for formulastr in formulastrs:
                try:
                    fe.generate_features(formulastr)
                except Exception as e:
                    err_obj = {"id": keypoint.id, "formula": formulastr,
                               "error": str(e)}
                    broken.append(err_obj)
                    print(err_obj)
        except Exception as e:
            err_obj = {"id": keypoint.id, "keypoint_content": keypoint.content,
                       "error": str(e)}
            broken.append(err_obj)
            print(err_obj)

    with open('keypoint_errors.json', 'w') as fp:
        json.dump(broken, fp, indent=2)

    return broken


def check_solution_content():
    solutions = Solution.objects.all()
    broken = []

    for solution in solutions:
        formulastrs = apiv2.search.utils.formula_extractor.extract_formulas_from_text(solution.content)

        try:
            for formulastr in formulastrs:
                try:
                    fe.generate_features(formulastr)
                except Exception as e:
                    err_obj = {"id": solution.id, "formula": formulastr,
                               "error": str(e)}
                    broken.append(err_obj)
                    print(err_obj)
        except Exception as  e:
            err_obj = {"id": solution.id, "solution_content": solution.content,
                       "error": str(e)}
            broken.append(err_obj)
            print(err_obj)

    with open('solution_errors.json', 'w') as  fp:
        json.dump(broken, fp, indent=2)

    return broken


def find_integral_sup():
    questions = Question.objects.filter(content__iregex=r'\\int\^.+')
    return questions


def find_sqrt():
    questions = Question.objects.filter(content__iregex=r'\\sqrt\[.+')
    return questions


pattern = r'(?<!.*(sqrt|array))['

def fix_integral_sup():
    questions = find_integral_sup()

    for question in questions:
        question.content = corrected.get(question.id)
        question.save()
        print("question %s is fixed" % question.id)


def fix_sqrt():
    questions = find_sqrt()
    for question in questions:
        fixed = corrected.get(question.id)
        if fixed:
            question.content = fixed
            question.save()
            print("Question %s is saved" % question.id)


def fix_integral_sup():
    questions = find_integral_sup()

    for question in questions:
        question.content = corrected.get(question.id)
        question.save()
        print("question %s is fixed" % question.id)

corrected = {'id': 'corrected_content'}


def fix_questions():
    for q_id in corrected:
        question = Question.objects.get(pk=q_id)
        question.content = corrected[q_id]
        question.save()
        print("question %s is fixed" % question.id)


# handle integral
# handle []:
# escape except exceptions
# fix exceptions: do not stop if error parsing is found
