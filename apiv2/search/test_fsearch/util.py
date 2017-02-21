import itertools
import os

from apiv2.models import TestQuestion

try:
   import cPickle as pickle
except:
   import pickle


TXT_FILE = os.path.join(os.path.dirname(__file__), 'test_q.txt')
MQID_PICKLE_FILE = os.path.join(os.path.dirname(__file__), "map_qids.pickle")
QID_PICKLE_FILE = os.path.join(os.path.dirname(__file__), "qids.pickle")


def read_test_questions_mids():
    file_exist = os.path.isfile(MQID_PICKLE_FILE)
    if not file_exist: write_test_questions_to_pickle()
    with open(MQID_PICKLE_FILE, mode='rb') as f:
        mqids = pickle.load(f)
    return mqids


def read_test_question_ids():
    file_exist = os.path.isfile(QID_PICKLE_FILE)
    if not file_exist: write_test_questionids_to_pickle()
    with open(QID_PICKLE_FILE, mode='rb') as f:
        qids = pickle.load(f)
    return qids


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
    mqids = read_test_questions_mids()
    qids = list(itertools.chain.from_iterable(mqids[topic] for topic in mqids))
    with open(QID_PICKLE_FILE, mode="wb") as f:
        pickle.dump(qids, f)

    return qids


def get_questions_from_concept(concept):
    questions = TestQuestion.objects.filter(concept=concept)
    return questions


def get_test_questions_from_ids():
    qids = read_test_question_ids()
    questions = TestQuestion.objects.filter(pk__in=qids)
    return questions


def get_question_content(qids):
    question_content = {}
    for qid in qids:
        question = TestQuestion.objects.get(pk=qid)
        question_content[qid] = question.content

    return question_content