vowels = set('aeiou')
w = input('please write a word: ')

u = vowels.union(set(w))

d = vowels.difference(set(w))

i = vowels.intersection(set(w))

print(u, d, i)
