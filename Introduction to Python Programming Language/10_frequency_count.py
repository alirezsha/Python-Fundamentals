v = ['a', 'e', 'i', 'o', 'u']
w = input('please write a word: ')

vowels = {}

vowels['a'] = 0
vowels['e'] = 0
vowels['i'] = 0
vowels['o'] = 0
vowels['u'] = 0

for letter in w:
    if letter in v:
        vowels[letter] += 1
            
for k, v in vowels.items():
    print(k, 'was found', v, 'time(s).')