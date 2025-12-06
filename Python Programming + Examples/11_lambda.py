def diploid(n):
    return n*2

print(diploid(30))
print('---------------------------------')

dip = lambda n: n*2

print(dip(30))
print('---------------------------------')

add = lambda a, b: a+b

print(add(3, 6))
print('---------------------------------')

am = lambda a, b: (a+b, a-b)

print(am(3, 6))
print('---------------------------------')

d = {'x': 9, 'y': 13, 'z': 1}

print(d[max(d.keys(), key = (lambda k: d[k]))])
print('---------------------------------')

l = ['peter', 'mary', 'george']
u = []
for s in l:
    a = s.upper()
    u.append(a)

print(u)
print('---------------------------------')

m = map(str.upper, l)

print(list(m))
print('---------------------------------')

students = ['peter', 'mary', 'george']
scores = [19, 20, 16]

print(list(zip(students, scores)))
print('---------------------------------')

print(list(map(lambda a, b: (a, b), students, scores)))
print('---------------------------------')

l = ['x', 'y']
my_ascii = []
for i in l:
    my_ascii.append(ord(i))

print(my_ascii)
print('---------------------------------')

print(list(map(ord, l)))
print('---------------------------------')

grade = [20, 16, 7, 18, 13, 6]

print(list(map(lambda g: g > 10, grade)))
print('---------------------------------')

l1 = [3, 6, 9]
l2 = [13, 33, 10]

print(list(map(lambda a, b: a+b, l1, l2)))
print('---------------------------------')

def func(a):
    return a + 5

def func_(b):
    return b * 2

funcs = [func, func_]

l = [10, 11, 12, 13]

for n in l:
    print(list(map(lambda x: x(n), funcs)))

print('---------------------------------')

grade = [20, 16, 7, 18, 13, 6]

print(list(filter(lambda g: g > 10, grade)))
print('---------------------------------')

l = ['level', 'home', 'racecar', 'refer', 'cash']
palindrome = lambda x: (x == ''.join(reversed(x)))

print(list(filter(palindrome, l)))
print('---------------------------------')

print(list(map(palindrome, l)))
print('---------------------------------')

l =[9, 8, '', 13, {}, 1, []]

print(list(filter(None, l)))
print('---------------------------------')

from functools import reduce

l = [6, 7, 9, 3, 1]

print(reduce(lambda x, y: x+y, l))
print('---------------------------------')

l = [13, 1, 3, 9, 8, 6]
l_sorted = sorted(l)

print(l_sorted)
print('---------------------------------')

l.sort()

print(l)
print('---------------------------------')

stu = [{'id': 25339, 'name': 'mark', 'score': 20}, 
       {'id': 25169, 'name': 'george', 'score': 17}, 
       {'id': 25908, 'name': 'mary', 'score': 9},
       {'id': 25913, 'name': 'peter', 'score': 19},
       {'id': 25936, 'name': 'scarlett', 'score': 20}]

l = lambda x: x['score']

print(sorted(stu, key = l))
print('---------------------------------')

from operator import itemgetter

stu = [(25339, 'mark', 20), 
       (25169, 'george', 17), 
       (25908, 'mary', 9),
       (25913, 'peter', 19),
       (25936, 'scarlett', 20)]

print(sorted(stu, key = itemgetter(2)))
print('---------------------------------')

print(sorted(stu, key = itemgetter(2), reverse=True))
print('---------------------------------')

print(sorted(stu, key = itemgetter(2, 0)))
