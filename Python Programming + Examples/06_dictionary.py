d = {'name': 'maryam',
     'country': 'iran',
     'field': 'mathematics'}

print(type(d))
print(len(d))
print('---------------------------------')

d = dict(name = 'maryam', country = 'iran', field = 'mathematics')

print(type(d))
print(len(d))
print('---------------------------------')

d = {'name': 'maryam',
     'country': 'iran',
     'field': 'mathematics'}

d['achievement'] = 'fields medal'

print(d)
print()
print(type(d))
print(len(d))
print()
print(d['field'])
print('---------------------------------')

x = d.get('name')

print(x)
print('---------------------------------')

x = d.get('job')

print(x)
print('---------------------------------')

print(d.keys())
print('---------------------------------')

print(d.values())
print('---------------------------------')

print(list(d.keys()))
print('---------------------------------')

print(list(d.values()))
print('---------------------------------')

print(list(d.items()))
print('---------------------------------')

for k, v in d.items():
    print(k, ':', v)

print('---------------------------------')

d.pop('country')

print(d)
print('---------------------------------')

d.popitem()

print(d)
print('---------------------------------')

d.popitem()

print(d)
print('---------------------------------')

d.clear()

print(d)
print('---------------------------------')

del d
print('---------------------------------')

l = ['a', 'b', 'c', 'a', 'd', 'c']
d = {}

for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)
print('---------------------------------')

d = {}

for i in l:
    d[i] = d.get(i, 0) + 1
    
print(d)
print('---------------------------------')

d2 = d.copy()

print(d2)
print('---------------------------------')

del d
del d2
print('---------------------------------')

s = 'united states of america'
d = {}

for i in s:
    d[i] = d.get(i, 0) + 1

print(d)
print('---------------------------------')

del d
print('---------------------------------')

content = 'a dictionary is a datastructure.'
d = {}
l = content.split()

print(l)

for i in l:
    d[i] = d.get(i, 0) + 1

print(d)
print('---------------------------------')

del d
print('---------------------------------')

d = {'a': 2, 'b': 1, 'c': 2, 'd': 1}
a = 0

for i in d:
    a += d[i]

print(a)
print('---------------------------------')

print(sum(d.values()))
print('---------------------------------')

del d
print('---------------------------------')

d = {'a': 6, 'b': 1, 'c': 3, 'd': 100, 'e': 69}
import operator

k = operator.itemgetter(1)

print(sorted(d.items(), key= k))
print('---------------------------------')

d = {'c': 6, 'e': 1, 'd': 3, 'a': 100, 'b': 69}
k = operator.itemgetter(0)

print(sorted(d.items(), key= k))
print('---------------------------------')

del d
print('---------------------------------')

stu = {'mike': [20, 16, 19, 20],
       'mary': [19, 19, 20, 13],
       'bill': [18, 15, 17, 19],
       'alex': [16, 20, 17, 16]}
d = {k: sorted(v) for k, v in stu.items()}

print(d)
print('---------------------------------')

del d
del stu
print('---------------------------------')

d1 = {'a': 6, 'b': 1, 'c': 3, 'd': 9}
d2 = {'x': 100, 'y': 1}

d = {}
d = d1.copy()
d.update(d2)

print(d)
print('---------------------------------')

for i in (d1, d2):
    d.update(i)

print(d)
print('---------------------------------')

d = {**d1, **d2}

print(d)
print('---------------------------------')

del d
del d1
del d2
del i
print('---------------------------------')

k = ['mary', 'bill']
v = ['stanford', 'mit']

z = zip(k, v)
d = dict(z)

print(d)
print('---------------------------------')

del d
print('---------------------------------')

s = 'united states of america'
ch = ['s', 'a']
d = {}

for i in s:
    if i in ch:
        d.setdefault(i, 0)
        d[i] += 1

print(d)
print('---------------------------------')

del d
print('---------------------------------')

d = {'a': 6, 'b': 1, 'c': 3, 'b': 1, 'c': 9}
o = {}

for k, v in d.items():
    if v not in o.values():
        o[k] = v

print(o)
print('---------------------------------')

del d
del o
print('---------------------------------')

d = {'lion': 0,
     'line': 0}

import random

for i in range(13):
    d[random.choice(list(d.keys()))] += 1
    
print(d)
print('---------------------------------')

del d
print('---------------------------------')

stu = [{'id': 25369, 'name': 'mark', 't/f': False}, 
       {'id': 25139, 'name': 'george', 't/f': True}, 
       {'id': 25936, 'name': 'mary', 't/f': True}]

print(sum(d['t/f'] for d in stu))
print('---------------------------------')

print(stu[0])
print('---------------------------------')

del stu
print('---------------------------------')

house = {'dad': {'name': 'alex', 'age': 27},
         'mom': {'name': 'jasmin', 'age': 27}}

print(house)
print('---------------------------------')

dad = {'name': 'alex', 'age': 27}
mom = {'name': 'jasmin', 'age': 27}
house = {'dad': dad,
         'mom': mom}

print(house)
print('---------------------------------')

del dad
del mom
del house
print('---------------------------------')

call_number = {'mob': +1123456789,
              'home': +1987654321}

person = {'name': 'george',
           'age': '29',
           'parent': ['mary', 'joe'],
           'phone': call_number}

print(len(person))
print(person['phone'])
print(person['phone']['hoe'])
print(person['parent'][1])
print()
print(person.pop('age'))
