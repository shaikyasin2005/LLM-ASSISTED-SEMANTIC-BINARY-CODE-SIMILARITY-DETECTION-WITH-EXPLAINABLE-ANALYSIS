from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def tfidf_similarity(code1: str, code2: str):

    """
    Compute semantic similarity between two code snippets using TF-IDF
    """

    if not code1 or not code2:
        return 0.0

    documents = [code1, code2]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return float(similarity_matrix[0][0])