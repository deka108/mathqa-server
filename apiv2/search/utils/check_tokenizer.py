from apiv2.search.utils import formula_extractor as fe
from apiv2.search.utils import formula_features_extractor as ffe
from apiv2.models import *

import json
import os
import itertools

try:
   import cPickle as pickle
except:
   import pickle

TXT_FILE = os.path.join(os.path.dirname(__file__), 'test_q.txt')
MQID_PICKLE_FILE = os.path.join(os.path.dirname(__file__), "map_qids.pickle")
QID_PICKLE_FILE = os.path.join(os.path.dirname(__file__), "qids.pickle")
JSON_FILE = os.path.join(os.path.dirname(__file__), "%s") + ".json"


def read_test_questions():
    file_exist = os.path.isfile(MQID_PICKLE_FILE)
    if not file_exist: write_test_questions_to_pickle()
    with open(MQID_PICKLE_FILE, mode='rb') as f:
        mqids = pickle.load(f)
    return mqids


def read_test_questionids():
    file_exist = os.path.isfile(QID_PICKLE_FILE)
    if not file_exist: write_test_questionids_to_pickle()
    with open(QID_PICKLE_FILE, mode='rb') as f:
        qids = pickle.load(f)
    return qids


def check_test_questions():
    test_questions = read_test_questions()
    for test_q in test_questions:
        check_question_token_from_question_ids(test_questions[test_q], True,
                                               test_q)
        print(test_q + " is written!")
    print("Success!")


def write_test_questions_to_pickle():
    with open(TXT_FILE, mode='r') as f:
        test_questions = f.read()

    topics = test_questions.split("\n\n")
    topics = [topic.split('\n') for topic in topics]
    test_questions = {topic[0]: [q for q in topic[1].split()] for topic in
                      topics}

    with open(MQID_PICKLE_FILE, mode="wb") as f:
        pickle.dump(test_questions, f)

    return test_questions


def write_test_questionids_to_pickle():
    mqids = read_test_questions()
    qids = list(itertools.chain.from_iterable(mqids[topic] for topic in mqids))
    with open(QID_PICKLE_FILE, mode="wb") as f:
        pickle.dump(qids, f)

    return qids


def check_question_from_concepts(concepts):
    for concept in concepts:
        check_question_token_from_concept(concept)


def get_questions(concept):
    questions = Question.objects.filter(concept=concept)
    return questions


def check_question_token_from_concept(concept):
    questions = get_questions(concept)
    return check_question_token_from_questions(questions)


def get_test_questions_from_ids():
    qids = read_test_questionids()
    questions = Question.objects.filter(pk__in=qids)
    return questions


def check_question_token_from_question_ids(question_ids, write_to_file=False,
                                        file_name=None):
    question_formula_mathml = {}
    for qid in question_ids:
        question = Question.objects.get(pk=qid)
        question_formula_mathml[question.id] = {
            "content": question.content,
            "math_ml_formulas": formula_mathmlstr(question.content)
        }

    if write_to_file and file_name:
        with open(JSON_FILE %file_name, mode="w") as f:
            json.dump(question_formula_mathml, f , indent=2)

    return question_formula_mathml


def check_question_token_from_questions(questions, write_to_file=False,
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


def get_question_content(qids):
    question_content = {}
    for qid in qids:
        question = Question.objects.get(pk=qid)
        question_content[qid] = question.content

    return question_content


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