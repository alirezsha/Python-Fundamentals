v = ['a', 'e', 'i', 'o', 'u']
#w = 'artificial intelligence'
w = input('please write a word: ')

vowels = []

for letter in w:
    if letter in v:
        if letter not in vowels:
            vowels.append(letter)
            
for vowel in vowels:
    print(vowel)
