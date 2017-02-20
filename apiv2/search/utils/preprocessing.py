from apiv2.models import *
import nltk
import re


def clean_text(text):
    # detect formula --> regex
    # remove formula
    pass


def add_tag(text):
    # detect formula function
    # add tag
    pass


# Full text index search
# Preprocess question text
    # Recognise and remove LaTeX
    # Convert to lower case
    # Remove non alphabetical characters
    # Remove stopwords

def preprocess(query):
    query = re.sub(r'[^w]', query)
    query = query.lower()
    return query