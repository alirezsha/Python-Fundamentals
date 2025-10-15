def letter_detection(phrase : str, letters : str = 'aeiou') -> set:
    """This function returns the set of letters found in the phrase."""

    return set(letters).intersection(set(phrase))
