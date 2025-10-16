def print_phrase(phrase, a):
    if a <= 0:
        return
    print(phrase)
    print_phrase(phrase, a-1)
    