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
    (NUMERIC, 'Numbers'),
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

# DIFFICULTIES = [
#     ("1", 'Very Easy'),
#     ("2", 'Easy'),
#     ("3", 'Average'),
#     ("4", 'Difficult'),
#     ("5", 'Very Difficult'),
# ]

DIFFICULTIES = [
    ("1", 'Very Easy'),
    ("2", 'Easy'),
    ("3", 'Easy'),
    ("4", 'Average'),
    ("5", 'Average'),
    ("6", 'Average'),
    ("7", 'Difficult'),
    ("8", 'Difficult'),
    ("9", 'Very Difficult'),
    ("10", 'Very Difficult'),
]

MARKS = [(i, i) for i in range(10)]

CONTEST_TIME = [
    ("1", '1 minute per question '),
    ("2", '2 minutes per question'),
]

NUMER_OF_QUESTIONS = [
    ("5", '5'),
    ("10", '10'),
    ("15", '15'),
    ("20", '20'),
]
