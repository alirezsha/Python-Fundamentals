def vowel_detection():
    """This function shows the vowels in the word."""
    v = set('aeiou')
    w = input('please write a word: ')

    vowels = v.intersection(set(w))

    for vowel in vowels:
        print(vowel)
        