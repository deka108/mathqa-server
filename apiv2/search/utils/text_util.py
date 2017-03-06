from apiv2.models import *
from apiv2.search.utils import formula_extractor as fe
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

import re

cachedStopWords = stopwords.words("english")
english_vocab = set(w.lower() for w in words.words())
stemmer = SnowballStemmer("english")


def clean_text(text):
    # detect formula --> regex
    # remove formula
    pass


# def add_tag(text):
    # detect formula function
    # add tag

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


def preprocess(text, stem=True):
    preprocessed_text = text

    # Recognise and remove LaTeX (detect formula function)
    preprocessed_text = re.sub(fe.DOUBLE_DOLLAR_NOTATION, " ", preprocessed_text)
    preprocessed_text = re.sub(fe.PAREN_NOTATION, " ", preprocessed_text)
    preprocessed_text = re.sub(fe.BRACKET_NOTATION, " ", preprocessed_text)

    # Remove non alphabetical characters
    preprocessed_text = re.sub(r'[^a-zA-Z]', " ", preprocessed_text)

    # Convert to lower case
    preprocessed_text = to_lower(preprocessed_text)

    # Remove stopwords
    preprocessed_text = remove_stopwords(preprocessed_text)

    # Filter words
    preprocessed_text = english_only(preprocessed_text)

    if stem:
        preprocessed_text = stem_text(preprocessed_text)

    return preprocessed_text


def preprocess_questions(stem=True):
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


if __name__ == '__main__':
    preprocess_questions()