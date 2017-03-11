import json

from apiv2.models import *
from apiv2.search.fsearch import formula_features_extractor as ffe
from apiv2.search.test_fsearch.utils import test_questions_util
from apiv2.search.test_fsearch.utils.paths import JSON_FILE
from apiv2.search.fsearch import formula_extractor as fe


def check_question_from_concepts(concepts):
    for concept in concepts:
        check_question_token_from_concept(concept)


def check_question_token_from_concept(concept):
    questions = test_questions_util.get_questions_from_concept(concept)
    return check_question_token_from_questions(questions)


def check_test_questions():
    test_questions = test_questions_util.read_test_questions_mids()
    for topic in test_questions:
        check_question_token_from_question_ids(test_questions[topic], True,
                                               topic)
        print(topic + " is written!")
    print("Success!")


def check_question_token_from_question_ids(question_ids, write_to_file=True,
                                        file_name=None):
    question_formula_mathml = {}
    for qid in question_ids:
        question = TestQuestion.objects.get(pk=qid)
        question_formula_mathml[question.id] = {
            "content": question.content,
            "math_ml_formulas": formula_mathmlstr(question.content)
        }

    if write_to_file and file_name:
        with open(JSON_FILE %file_name, mode="w") as f:
            json.dump(question_formula_mathml, f , indent=2)

    return question_formula_mathml


def check_question_token_from_questions(questions, write_to_file=True,
                                        file_name="random"):
    question_formula_mathml = {}
    for question in questions:
        question_formula_mathml[question.id] = {
            "content": question.content,
            "math_ml_formulas": formula_mathmlstr(question.content)
        }

    if write_to_file:
        with open(file_name + ".json", mode="w") as f:
            json.dump(question_formula_mathml, f)

    return question_formula_mathml


def formula_mathmlstr(text):
    formulas = fe.extract_formulas_from_text(text)
    formula_mathmls = {}

    for formula in formulas:
        formula_mathmls[formula] = (ffe._generate_mathmlstr(formula).decode(
            'string_escape'))

    return formula_mathmls

concepts = [5, 15, 22, 24, 32, 36, 38, 42, 43]

if __name__ == "__main__":
    check_test_questions()