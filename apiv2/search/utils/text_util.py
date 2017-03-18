import re
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.stem.snowball import SnowballStemmer

from apiv2.models import QuestionText, Question
from apiv2.search.fsearch import formula_extractor as fe

cachedStopWords = stopwords.words("english")
english_vocab = set(w.lower() for w in words.words())
stemmer = SnowballStemmer("english")


# Full text index search
def to_lower(text):
    return ' '.join([word.lower() for word in text.split()])


def remove_stopwords(text):
    return ' '.join([word for word in text.split() if len(word) > 2 and word
                     not in cachedStopWords])


def english_only(text):
    return ' '.join([word for word in text.split() if word in english_vocab])


def stem_text(text):
    return ' '.join([stemmer.stem(word) for word in text.split()])


def preprocess(text, **kwargs):
    preprocessed_text = text

    # Recognise and remove LaTeX (detect formula function)
    preprocessed_text = clean_latex(preprocessed_text)

    # Remove non alphabetical characters
    preprocessed_text = remove_non_alphabet(preprocessed_text)

    # Convert to lower case
    preprocessed_text = to_lower(preprocessed_text)

    # Remove stopwords
    preprocessed_text = remove_stopwords(preprocessed_text)

    # Filter words
    if kwargs.get("english", True):
        preprocessed_text = english_only(preprocessed_text)

    if kwargs.get("stem", True):
        preprocessed_text = stem_text(preprocessed_text)

    return preprocessed_text


def preprocess_unique(text, **kwargs):
    results = preprocess(text, **kwargs).split()
    return ' '.join(set(results))


def remove_non_alphabet(text):
    text = re.sub(r'[^a-zA-Z]', " ", text)
    return text


def clean_latex(text):
    text = re.sub(fe.DOUBLE_DOLLAR_NOTATION, " ", text)
    text = re.sub(fe.PAREN_NOTATION, " ", text)
    text = re.sub(fe.BRACKET_NOTATION, " ", text)
    return text


def preprocess_query(text):
    text = preprocess(text)

    return text


def preprocess_question_text_object(stem=True):
    QuestionText.objects.all().delete()
    questions = Question.objects.all()
    for question in questions:
        preprocessed_text = preprocess(question.content, stem)
        print(preprocessed_text)
        question_text = QuestionText(
            content=preprocessed_text,
            question=question
        )
        question_text.save()