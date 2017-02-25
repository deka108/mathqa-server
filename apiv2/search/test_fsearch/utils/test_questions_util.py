import itertools

import os

from apiv2.search.test_fsearch.utils import paths

try:
   import cPickle as pickle
except:
   import pickle

from apiv2.models import TestQuestion, Question


def insert_test_questions(reset=True):
    test_questions = read_test_questions_mids()

    if reset:
        TestQuestion.objects.all().delete()

    for topic in test_questions:
        print(topic)
        for test_id in test_questions[topic]:
            question = Question.objects.get(pk=test_id)
            new_test_question = TestQuestion(
                id=question.id,
                category=topic,
                marks=question.marks,
                difficulty_level=question.difficulty_level,
                source = question.source,
                content=question.content,
                concept=question.concept,
                subconcept=question.subconcept,
                paper = question.paper
            )
            new_test_question.save()


def reset_questions():
    write_test_questions_to_pickle()
    write_test_questionids_to_pickle()

    insert_test_questions()


def read_test_questions_mids():
    file_exist = os.path.isfile(paths.MQID_PICKLE_FILE)
    if not file_exist: write_test_questions_to_pickle()
    with open(paths.MQID_PICKLE_FILE, mode='rb') as f:
        mqids = pickle.load(f)
    return mqids


def read_test_question_ids():
    file_exist = os.path.isfile(paths.QID_PICKLE_FILE)
    if not file_exist: write_test_questionids_to_pickle()
    with open(paths.QID_PICKLE_FILE, mode='rb') as f:
        qids = pickle.load(f)
    return qids


def write_test_questions_to_pickle():
    with open(paths.TXT_FILE, mode='r') as f:
        test_questions = f.read()

    topics = test_questions.split("\n\n")
    topics = [topic.split('\n') for topic in topics]
    test_questions = {topic[0]: [q for q in topic[1].split()] for topic in
                      topics}

    with open(paths.MQID_PICKLE_FILE, mode="wb") as f:
        pickle.dump(test_questions, f)

    return test_questions


def write_test_questionids_to_pickle():
    mqids = read_test_questions_mids()
    qids = list(itertools.chain.from_iterable(mqids[topic] for topic in mqids))
    with open(paths.QID_PICKLE_FILE, mode="wb") as f:
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


def get_test_question_info():
    mqids = read_test_questions_mids()
    overall_info = "Total topic: %s" % len(mqids)
    total_questions = 0

    with open(paths.INFO_FILE, mode='w') as f:
        print(overall_info)
        f.write(overall_info + "\n")
        for topic in mqids:
            total_question = len(mqids[topic])
            total_questions += total_question

            topic_info = "%s: %s" % (topic, str(total_question))
            print(topic_info)
            f.write(topic_info)
            f.write("\n")

        total = "Total questions: %s" % str(total_questions)
        print(total)
        f.write(total)

