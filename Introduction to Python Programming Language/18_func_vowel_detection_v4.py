def vowel_detection(word):
    """This function returns every vowel found in the word."""
    v = set('aeiou')
    
    vowels = v.intersection(set(word))

    return vowels
