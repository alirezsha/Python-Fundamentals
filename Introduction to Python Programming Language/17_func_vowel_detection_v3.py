def vowel_detection(word):
    """This function returns a boolean if the word contains vowels."""
    v = set('aeiou')
    
    vowels = v.intersection(set(word))

    return bool(vowels)
