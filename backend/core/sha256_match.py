import hashlib


def calculate_hash(file_path):

    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def check_exact_match(file1, file2):

    # Source vs source
    if file1.endswith(".c") and file2.endswith(".c"):
        return calculate_hash(file1) == calculate_hash(file2)

    # Binary vs binary
    if file1.endswith(".exe") and file2.endswith(".exe"):
        return calculate_hash(file1) == calculate_hash(file2)

    # Different types cannot be exact match
    return False