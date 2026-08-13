import re


def preprocess_code(code: str) -> str:
    """
    Clean and normalize decompiled code before similarity computation
    """

    if not code:
        return ""

    code = code.lower()

    # Remove single line comments
    code = re.sub(r"//.*", "", code)

    # Remove multi-line comments
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.S)

    # Remove string literals
    code = re.sub(r'"[^"]*"', "", code)

    # Remove numbers
    code = re.sub(r"\d+", "", code)

    # Normalize whitespace
    code = re.sub(r"\s+", " ", code)

    return code.strip()