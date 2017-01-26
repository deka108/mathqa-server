"""
# Name:           check_answer_api/utilities/text_similarity_checker.py
# Description:
# Created by:     Martinus Alexander
# Date Created:   Dec 24, 2016
# Last Modified:  Jan 19, 2017
# Modified by:    Martinus Alexander
"""

import numpy as np
import re
import string

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer

from ngram import NGram

overall_threshold = 0.7
gram = 3

"""
Check the similarity between 2 text.
"""
def check(standard_answer, user_answer):
	global overall_threshold
	# Remove the punctuation
	standard_answer = "".join(char for char in standard_answer if char not in string.punctuation)
	user_answer = "".join(char for char in user_answer if char not in string.punctuation)
	if len(re.split(" ", standard_answer)) < 3 or len(re.split(" ", user_answer)) < 3:
		# Too short string, implement using simple string matching
		standard_answer_list = re.split(" ", standard_answer)
		user_answer_list = re.split(" ", user_answer)
		# Remove duplicates, then sort
		standard_answer_list = list(set(standard_answer_list)).sort()
		user_answer_list = list(set(user_answer_list)).sort()
		correctness = (standard_answer_list == user_answer_list)
		return correctness
	# Perform Latent semantic analysis on the answer
	lsa_score, lsa_error = lsa_test(standard_answer, user_answer)
	# Perform N-Gram analysis on the answer
	ngram_score, ngram_error = ngram_test(standard_answer, user_answer)
	# Perform set operation analysis on the answer
	set_operation_score, set_operation_error = set_operation_test(standard_answer, user_answer)
	total_score = 0
	n_model = 0
	if lsa_error == None:
		total_score = total_score + lsa_score
		n_model = n_model + 1
	if ngram_error == None:
		total_score = total_score + ngram_score
		n_model = n_model + 1
	if set_operation_error == None:
		total_score = total_score + set_operation_score
		n_model = n_model + 1
	if n_model == 0:
		return False
	else:
		return ((total_score * 1.0 / n_model) > overall_threshold)


def lsa_test(standard_answer, user_answer):
	try:
		data = [standard_answer, user_answer]
		vectorizer = CountVectorizer(min_df=1, stop_words='english')
		dtm = vectorizer.fit_transform(data)
		# print(vectorizer.get_feature_names())
		lsa = TruncatedSVD(n_components=2, algorithm="randomized")
		dtm_lsa = lsa.fit_transform(dtm)
		dtm_lsa = Normalizer(copy=False).fit_transform(dtm_lsa)
		similarity = np.asarray(np.asmatrix(dtm_lsa) * np.asmatrix(dtm_lsa).T)
		return similarity[0][1], None
	except ValueError:
		return -1, ValueError


def ngram_test(standard_answer, user_answer):
	global gram
	try:
		score = NGram.compare(standard_answer, user_answer, N=gram)
		return score, None
	except:
		return -1, ValueError

def set_operation_test(standard_answer, user_answer):
	try:
		standard_answer_list = re.split(" ", standard_answer)
		user_answer_list = re.split(" ", user_answer)
		standard_answer_ngram = NGram(standard_answer_list)
		user_answer_ngram = NGram(user_answer_list)
		intersection = list(standard_answer_ngram.intersection(user_answer_ngram))
		n_match = len(intersection)
		score = 1.0 * n_match / len(standard_answer_list)
		return score, None
	except:
		return -1, ValueError


"""
-----------------------------------------------------------------------------------------
CODE BELOW ARE UNUSED
"""

"""
UNUSED
Reference:
http://www.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
def check(standard_text, user_answer):
	# Tokenization process
	tokens = get_tokens(standard_text)
	# Stop word removal
	tokens_without_stopwords = remove_stop_words(tokens)
	# Stemming
	stem_tokens(WordNetLemmatizer(), tokens_without_stopwords)
	vector = TfidfVectorizer(tokenizer=get_tokens, stop_words='english')
	tfidf = vector.fit_transform([standard_text, user_answer])
	print((tfidf * tfidf.T).A[0][1])
	return  (tfidf * tfidf.T).A[0][1] > 0.6
"""

"""
Tokenization
"""
def get_tokens(input_text):
	input_text_lower = input_text.lower()
	# Remove punctuation using the character deletion step of translate
	input_text_no_punctuation = "".join(char for char in input_text_lower if char not in string.punctuation)
	tokens = nltk.word_tokenize(input_text_no_punctuation, language="english")
	return tokens

"""
Stop words removal
"""
def remove_stop_words(tokens):
	tokens_without_stopwords = [word for word in tokens if word not in stopwords.words("english")]
	return tokens_without_stopwords

"""
Stemming (currently implemented with Lemmatization)
"""
def stem_tokens(stemmer, tokens):
	stemmed_tokens = []
	for token in tokens:
		stemmed_token = stemmer.lemmatize(token)
		stemmed_tokens.append(stemmed_token)
	return stemmed_tokens

"""
Reference:
http://stackoverflow.com/a/2754261
"""
def cosine_similarity(u, v):
	cosine_similarity = numpy.dot(u, v) / math.sqrt(numpy.dot(u, u) * numpy.dot(v, v))
	return cosine_similarity

def ngrams(sequence, n, pad_left=False, pad_right=False, pad_symbol=False):
	if pad_left:
		sequence = chain((pad_symbol,) * (n - 1), sequence)
	if pad_right:
		sequence = chain(sequence, (pad_symbol,) * (n - 1))
	sequence = list(sequence)
	count = max(0, len(sequence) - n + 1)
	return [tuple(sequence[i:i + n]) for i in range(count)]