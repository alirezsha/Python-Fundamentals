s = {'melon', 'strawberry', 'apple'}

print(type(s))
print(len(s))
print()
print(s)
print('---------------------------------')

for i in s:
    print(i)

print('---------------------------------')

s1 = set(('melon', 'strawberry', 'apple'))

print(s1)
print(s == s1)
print('---------------------------------')

print('banana' in s)
print('---------------------------------')

s.add('banana')

print(s)
print('---------------------------------')

s.update(['cherry', 'mango'])

print(s)
print('---------------------------------')

s.remove('melon')

print(s)
print('---------------------------------')

vowels = {'a', 'e', 'i', 'o', 'u'}

print(vowels)
print('---------------------------------')

vowels.discard('z')

print(vowels)
print('---------------------------------')

x = vowels.pop()

print(x)
print(vowels)
print('---------------------------------')

y = vowels.copy()

print(y)
print('---------------------------------')

vowels.clear()

print(vowels)
print(len(vowels))
print('---------------------------------')

del y
print('---------------------------------')

x = {1, 3, 6, 9, 13}
y = {3, 9, 100}

print(x-y)
print()
print(y-x)
print('---------------------------------')

d = x.difference(y)

print(d)
print(x)
print(y)
print('---------------------------------')

d = x.difference_update(y)

print(d)
print(x)
print(y)
print('---------------------------------')

a = {0, 1, 9, 6}
b = {9, 6, 3}

print(a.symmetric_difference(b))
print('---------------------------------')

print(a^b)
print('---------------------------------')

print(a.intersection(b))
print('---------------------------------')

print(a&b)
print('---------------------------------')

print(a.union(b))
print('---------------------------------')

print(a|b)
print('---------------------------------')

a.update(b)

print(a)
print('---------------------------------')

a = {69, 90}
s = 'mary'
l = [1, 100]
t = (666, 13)
d = {'ten': 10, 'twenty': 20}

a.update(s, l, t, d)

print(a)
print('---------------------------------')

a = {10, 20}
b = {10, 20, 30}

print(a.isdisjoint(b))
print('---------------------------------')

a = {10, 20}
b = {90, 100, 30}

print(a.isdisjoint(b))
print('---------------------------------')

a = {100, 36}
b = {100, 36, 1}

print(a.issubset(b))
print('---------------------------------')

print(b.issubset(a))
print('---------------------------------')

a = 'george'
d = {'e', 'g'}
s = set(a)

print(d.intersection(s))
print('---------------------------------')

d1 = {'a': 1, 'b': 6, 'c': 9, 'd': 3}
d2 = {'a': 1, 'b': 9, 'c': 3, 'd': 6}

s1 = set(d1.items())
s2 = set(d2.items())

s = s1&s2

for k, v in s:
    print(k)

