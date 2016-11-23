"""
# Name:           meas_models/common.py
# Description:
# Created by:     Phuc Le-Sanh
# Date Created:   N.A
# Last Modified:  Nov 21 2016
# Modified by:    Phuc Le-Sanh
"""
NUMERIC = 'Numberic'
SKETCH = 'Sketch'
EXPRESSION = 'EXPRESSION'
TEXT = 'Text'
PROVE = 'Prove'

RESPONSE_TYPES = [
    (NUMERIC, 'Exam Numberic'),
    (SKETCH, 'Sketch'),
    (EXPRESSION, 'Expression'),
    (TEXT, 'Text'),
    (PROVE, 'Prove')
]

PRACTICE_TEST = "PT"
CONTEST = "CT"

TEST_TYPES = [
    (PRACTICE_TEST, 'Practice Test'),
    (CONTEST, 'Contest')
]

QUESTION_TYPES = [
    ("EX", 'Exam'),
    ("PR", 'Practice')
]

QUESTION_SOURCES = [
    ("EP", 'Exam papers'),
    ("OL", 'Online')
]

USED_FOR = [
    ("NO", 'No'),
    ("ON", 'Online'),
    ("PA", 'Papers'),
    ("BO", 'Both online and papers')
]

NUMBER_OF_PARTS = [(i, i) for i in range(5)]

MONTHS = [
    ("1", 'January'),
    ("2", 'February'),
    ("3", 'March'),
    ("4", 'April'),
    ("5", 'May'),
    ("6", 'June'),
    ("7", 'July'),
    ("8", 'August'),
    ("9", 'September'),
    ("10", 'October'),
    ("11", 'November'),
    ("12", 'December')
]

DIFFICULTIES = [
    ("1", 'Very Easy'),
    ("2", 'Easy'),
    ("3", 'Average'),
    ("4", 'Difficult'),
    ("5", 'Very Difficult'),
]

MARKS = [(i, i) for i in range(10)]
