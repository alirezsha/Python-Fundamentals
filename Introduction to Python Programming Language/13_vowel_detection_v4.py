v = set('aeiou')
w = input('please write a word: ')

vowels = v.intersection(set(w))

for vowel in vowels:
    print(vowel)
    