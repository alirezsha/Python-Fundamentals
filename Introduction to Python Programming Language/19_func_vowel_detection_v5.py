def vowel_detection(word : str) -> set:
    """This function returns every vowel found in the word."""
    v = set('aeiou')

    return v.intersection(set(word))
