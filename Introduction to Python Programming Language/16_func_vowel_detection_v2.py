def vowel_detection(word):
    """This function shows the vowels in the word."""
    v = set('aeiou')
    
    vowels = v.intersection(set(word))

    for vowel in vowels:
        print(vowel)
        