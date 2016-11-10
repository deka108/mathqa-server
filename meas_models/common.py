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

NUMBER_OF_PARTS = [(i, i) for i in range(4)]

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
