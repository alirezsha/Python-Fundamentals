v = ['a', 'e', 'i', 'o', 'u']
w = input('please write a word: ')

vowels = {}

for letter in w:
    if letter in v:
        vowels.setdefault(letter, 0)
        vowels[letter] += 1
            
for k, v in vowels.items():
    print(k, 'was found', v, 'time(s).')