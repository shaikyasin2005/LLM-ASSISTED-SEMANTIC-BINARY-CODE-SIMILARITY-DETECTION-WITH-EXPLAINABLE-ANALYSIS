def generate_explanation(code1, code2, hybrid):

    hybrid = float(hybrid)

    if hybrid > 0.9:
        return (
            "The binaries are extremely similar. "
            "The control flow and instruction patterns indicate that both programs "
            "implement nearly identical computational logic."
        )

    elif hybrid > 0.7:
        return (
            "The binaries show strong similarity. "
            "Although implementation details differ slightly, both programs perform "
            "very similar operations and likely implement the same algorithm."
        )

    elif hybrid > 0.5:
        return (
            "The binaries share moderate similarity. "
            "Some structural patterns and instructions overlap, but the programs "
            "may use different techniques to achieve their functionality."
        )

    elif hybrid > 0.3:
        return (
            "The binaries show limited similarity. "
            "Only a small portion of the structure or instruction patterns match."
        )

    else:
        return (
            "The binaries appear to be significantly different and likely implement "
            "unrelated functionality."
        )