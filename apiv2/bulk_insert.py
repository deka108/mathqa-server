import os
import csv
from .models import *
from operator import itemgetter
from itertools import groupby

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
RELATIVE_DATA_PATH = "data_reconstruction/csv/"
DATA_PATH = os.path.join(BASE_PATH, RELATIVE_DATA_PATH)

file_names = {
    "edu": "education_level.csv",
    "subject": "subject.csv",
    "block": "block.csv",
    "topic": "topic.csv",
    "subtopic": "subtopic.csv",
    "keypoint": "keypoint.csv",
    "keypoint_tag": "keypoint_tag.csv",
    "keyword": "keyword.csv",
    "keyword_tag": "keyword_tag.csv",
    "tag": "tag",
    "paperset": "paperset.csv",
    "paper": "paper.csv",
    "question": "question.csv",
    "solution": "solution.csv",
    "formula": "formula.csv",
    "formula_index": "formula_index.csv",
    "image": "image.csv"
}


# ORDER:
def read_csv(file):
    data = []
    with open(os.path.join(DATA_PATH, file), 'rb') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
        return data


# Education Level
# Old: id, title, description
# New: id, name, description
def insert_edu_level():
    entries = read_csv(file_names["edu"])
    education_objects = [EducationLevel(id=int(entry['id']),
                                        name=entry['title'],
                                        description=entry['description'])
                         for entry in entries]
    EducationLevel.objects.bulk_create(education_objects)


# Subject
# Old: id, title, edu_level_id, description
# New: name, description, education_level
def insert_subject():
    entries = read_csv(file_names["subject"])
    print(entries)
    subject_objects = [Subject(id=int(entry['id']), name=entry['title'],
                               description=entry['description'],
                               education_level=
                               EducationLevel.objects.get(
                                   pk=int(entry['edu_level_id'])))
                       for entry in entries]
    Subject.objects.bulk_create(subject_objects)


# Topic
# Old: id,title,subject_id
# New: id,name, subject
def insert_topic():
    entries = read_csv(file_names["block"])
    topic_objects = [Topic(id=int(entry['id']),
                           name=entry['title'],
                           subject=Subject.objects.get(
                               id=entry['subject_id']))
                     for entry in entries]
    Topic.objects.bulk_create(topic_objects)


# Concept
# Old: id,block_id,title
# New: id,name,topic
def insert_concept():
    entries = read_csv(file_names["topic"])
    concept_objects = [Concept(id=int(entry['id']),
                           name=entry['title'],
                           topic=Topic.objects.get(
                               id=entry['block_id']))
                     for entry in entries]
    Concept.objects.bulk_create(concept_objects)


# Subconcept
# Old: id,topic_id,title
# New: id,concept,name
def insert_subconcept():
    entries = read_csv(file_names["subtopic"])
    subconcept_objects = [Subconcept(id=int(entry['id']),
                                     name=entry['title'],
                                     concept=Concept.objects.get(
                                         id=entry['topic_id']))
                          for entry in entries]
    Subconcept.objects.bulk_create(subconcept_objects)


# Keypoint
# Old: id,title,type,topic_id,content
# New: id,name,keypoint_type,content,concept
def insert_keypoint():
    entries = read_csv(file_names["keypoint"])
    keypoint_objects = [KeyPoint(id=int(entry["id"]),
                                 name=entry["title"],
                                 keypoint_type=entry["type"],
                                 content=entry["content"],
                                 concept=Concept.objects.get(
                                         id=entry['topic_id']))
                        for entry in entries]
    KeyPoint.objects.bulk_create(keypoint_objects)


# Keyword
# Old: id,title,type,topic_id,content
# New: id,name,content
def insert_keyword():
    entries = read_csv(file_names["keyword"])
    keyword_objects = [Keyword(id=int(entry["id"]),
                                 name=entry["title"],
                                 content=entry["content"])
                        for entry in entries]
    Keyword.objects.bulk_create(keyword_objects)


# Paperset
# Old: id,title,subject_id
# New: id,name,subject
def insert_paperset():
    entries = read_csv(file_names["paperset"])
    paperset_objects = [Paperset(id=int(entry['id']),
                                 name=entry['title'],
                                 subject=Subject.objects.get(
                                     id=entry['subject_id']))
                        for entry in entries]
    Paperset.objects.bulk_create(paperset_objects)


# Paper
# Old:id,year,month,number,subject_id,paperset_id
# New:id,year,month,number,no_of_question,subject,paperset
def insert_paper():
    entries = read_csv(file_names["paper"])
    paper_objects = [Paper(id=entry['id'],
                           year=int(entry['year']),
                           month=entry['month'],
                           number=int(entry['number']),
                           subject=Subject.objects.get(id=entry[
                               'subject_id']),
                           paperset=Paperset.objects.get(id=entry[
                               'paperset_id']))
                     for entry in entries]
    Paper.objects.bulk_create(paper_objects)


# Question
# Old:
    # Question: id,paper_id,question_no,content,topic_id,subtopic_id,marks,
        # source, difficulty

# New: id,question_type,used_for,marks,difficulty_level,response_type,
# source,content,concept,subconcept,paper,keypoints,keywords
def insert_question():
    entries = read_csv(file_names["question"])
    question_objects = [Question(id=entry['id'],
                                 marks=int(entry['marks']),
                                 difficulty_level=entry['difficulty'],
                                 source=entry['source'],
                                 content=entry['content'],
                                 concept=Concept.objects.get(
                                     id=entry['topic_id']),
                                 subconcept=Subconcept.objects.get(
                                     id=entry['subtopic_id']),
                                 paper=Paper.objects.get(
                                     id=entry['paper_id']),
                                 )
                        for entry in entries]
    Question.objects.bulk_create(question_objects)


# Tag: question_id,tagdefinition_id
# Notes: tag definition is now either keypoint or keyword
def update_question_keypoints():
    keypoints = read_csv(file_names["keypoint_tag"])
    keypoints.sort(key=itemgetter('question_id'))

    for question_id, group in groupby(keypoints, itemgetter('question_id')):
        question_object = Question.objects.get(id=question_id)
        keypoint_ids = [keypoint['tagdefinition_id'] for keypoint in group]
        keypoint_objects = KeyPoint.objects.filter(id__in=keypoint_ids)

        question_object.keypoints.clear()
        question_object.keypoints.add(*keypoint_objects)
        question_object.save()


def update_question_keywords():
    keywords = read_csv(file_names["keyword_tag"])
    keywords.sort(key=itemgetter('question_id'))

    for question_id, group in groupby(keywords, itemgetter('question_id')):
        question_object = Question.objects.get(id=question_id)
        keyword_ids = [keyword['tagdefinition_id'] for keyword in group]
        keyword_objects = Keyword.objects.filter(id__in=keyword_ids)

        question_object.keywords.add(*keyword_objects)
        question_object.save()


# Solution
# Old: id,question_id,content
# New: id,question,content
def insert_solution():
    entries = read_csv(file_names["solution"])
    solution_objects = [Solution(id=int(entry['id']),
                                 question=Question.objects.get(
                                     id=entry['question_id']),
                                 content=entry['content'])
                        for entry in entries]
    Solution.objects.bulk_create(solution_objects)


# Formula
def insert_formula():
    pass


# Formula Index
def insert_formula_index():
    pass


# Image
def insert_image():
    pass