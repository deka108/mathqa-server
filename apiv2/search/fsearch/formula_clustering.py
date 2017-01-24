from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans

import formula_transformer as ft
import os

SCRIPT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(SCRIPT_DIR, "../data")
FEATURES_FILE_PATH = os.path.join(DATA_PATH, "formula.feature")
VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.vector")
TFIDF_VECTOR_FILE_PATH = os.path.join(DATA_PATH, "formula.tfidf.vector")


# Source: http://scikit-learn.org/stable/auto_examples/text/document_clustering.html#sphx-glr-auto-examples-text-document-clustering-py


def get_formula_term():
    formula_feature_vectors = ft.read_normalized_tfidf_vectors()
    return formula_feature_vectors


def generate_kmeans_cluster(k=5):
    data = get_formula_term()
    kmeans_model = KMeans(n_clusters=k, random_state=42).fit(data)
    print(kmeans_model)


def generate_agglomerative_cluster(n=3):
    data = get_formula_term()
    model = AgglomerativeClustering(n_clusters=n, linkage="average",
                                    affinity="euclidean")
    model.fit(data)
    print(model)