def hybrid_similarity(tfidf_score, structural_score):
    """
    Combine semantic and structural similarity
    """

    return (0.6 * tfidf_score) + (0.4 * structural_score)