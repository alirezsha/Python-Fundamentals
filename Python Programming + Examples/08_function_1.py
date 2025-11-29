def greetings():
    print('Hello! What is going?')

greetings()
print('---------------------------------')

def hello():
    return 'Hello everybody!'

f = hello()
print(f)
print('---------------------------------')

def welcome(p):
    print(p)
    
a = 'Welcome to USA!'

welcome(a)
print('---------------------------------')

def summation(x, y):
    return x + y

print(summation(6, 9))
print('---------------------------------')

def double(p):
    p *= 2
    print(p)

double(3)
print('---------------------------------')

def maximum(x, y):
    if x > y:
        return x
    return y

print(maximum(30, 66))
print('---------------------------------')

def maximum_(x, y, z):
    return maximum(x, maximum(y, z))

print(maximum_(99, 36, 96))
print('---------------------------------')

from math import pi
#pi = 3.14159
def area(r):
     return pi * r * r
 
def circumference(r):
    return 2 * pi * r

def main():
    r = 6
    print(area(r))
    print(circumference(r))
    
main()
print('---------------------------------')

a = 3
def b():
    a = 9
    print(a)

b()
print(a)
print('---------------------------------')

a = 3
def b():
    global a
    a = 9
    print(a)

b()
print(a)
print('---------------------------------')

def func(x, y):
    x -= 1
    y += 1
    return x, y

a = 3
b = 9
alpha, beta= func(a, b)

print(alpha)
print(beta)
print('---------------------------------')

def func_(p):
    p[0] -= 1
    p[1] += 1
    
l = [3, 9]
func_(l)
print(l[0])
print(l[1])
print('---------------------------------')

def d(p):
    p['x'] -= 1
    p['y'] += 1
    
my_dict = {'x': 3, 'y': 9}
d(my_dict)
print(my_dict['x'])
print(my_dict['y'])
print('---------------------------------')

def func(x, y):
    print(x, y)
    
func(3, 6)
func(x = 3, y = 6)
func(3, y = 6)
print('---------------------------------')

def func_(x, y = 6, z = 9):
    print(x, y, z)
    
func_(7)
func_(7, 8)
func_(7, 8, 6)
func_(7, z = 13)
func_(y = 3, z = 6, x = 1)
print('---------------------------------')

def ka(*, x = 6):
    print(x)
    
ka()
ka(x = 3)
print('---------------------------------')

def va(*t):
    a = 0
    for i in t:
        a += i
    print(a)

va(3, 6, 9)
va(7, 8)
print('---------------------------------')

def add(x, y, *more):
    r = x + y + sum(more)
    print(r)
    
add(3, 6, 9)
add(7, 8)
add(3, 6, 13, 7, 1, 9)
print('---------------------------------')

def add(x, y, *more):
    print(more)
    
add(3, 6, 13, 7, 1, 9)
print('---------------------------------')

def func(*t, a = 3):
    print(a)
    print(t)
    
func(3, 6, a = 9)
func(3, 6)
func(3, 6, 8, 7)
print('---------------------------------')

def concat(*s, sep = '.'):
    return sep.join(s)

print(concat('mary', 'george'))
print(concat('mary', 'george', 'peter'))
print(concat('mary', 'george', 'peter', sep='/'))
print('---------------------------------')

def func(x, *, y = 3, z = 6):
    print(x, y, z)

func(7)
func(7, y = 9)
print('---------------------------------')

def func(x, y, **z):
    print(x, y, z)
    
func(1, 3, a=6, b=9)
print('---------------------------------')

def func(x, y, *z, **w):
    print(x, y, z, w)

func(1, 3, 16, 20, 10, a=6, b=9, z=13)
print('---------------------------------')

s = 'mAryMIrzaKHaNi'
count_dict = {'L': 0,
              'U': 0}

def f_count(s):
    for ch in s:
        if ch.islower():
            count_dict['L'] += 1
        else:
            count_dict['U'] += 1

f_count(s)
print(count_dict['L'])
print(count_dict['U'])
print('---------------------------------')

def ch_count(s):
    d = {}
    for ch in s:
        if ch in d.keys():
            d[ch] += 1
        else:
            d[ch] = 1
    return d

print(ch_count('United States of America'))
print('---------------------------------')

s = 'AI helps you be more productive.'
def w_count(s):
    d = {}
    words = s.split()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

print(w_count(s))
print('---------------------------------')

def switch(x):
    d = {3: 'three', 1:'one'}
    return d.get(x, 'nothing')

print(switch(3))
print(switch(1))
print(switch(13))
print(switch(2))
print('---------------------------------')

students_scores = [{'id': 1, 'midterm': 90, 'final': 100},
                   {'id': 2, 'midterm': 75, 'final': 85}]
def average(lst):
    for i in lst:
        sc1 = i.pop('midterm')
        sc2 = i.pop('final')
        i['average'] = (sc1 + sc2) / 2
    return lst

print(average(students_scores))
