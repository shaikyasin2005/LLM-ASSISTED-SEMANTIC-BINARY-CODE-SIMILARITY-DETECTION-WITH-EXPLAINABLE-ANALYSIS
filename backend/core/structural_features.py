import re


def extract_structural_features(code: str):

    features = {}

    features["if_count"] = len(re.findall(r"\bif\b", code))
    features["for_count"] = len(re.findall(r"\bfor\b", code))
    features["while_count"] = len(re.findall(r"\bwhile\b", code))
    features["return_count"] = len(re.findall(r"\breturn\b", code))
    features["function_calls"] = len(re.findall(r"\w+\(", code))

    return features


def structural_similarity(code1: str, code2: str):

    f1 = extract_structural_features(code1)
    f2 = extract_structural_features(code2)

    score = 0
    total = len(f1)

    for key in f1:

        v1 = f1[key]
        v2 = f2[key]

        if max(v1, v2) == 0:
            score += 1
        else:
            score += 1 - abs(v1 - v2) / max(v1, v2)

    return score / total