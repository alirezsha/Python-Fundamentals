t = ('Mathematic', 'Machine Learning', 'Programming', 'Business Analytics')

print(t)
print(type(t))
print(len(t))
print()
print(t[1])
print(t[0:2])
print(t.index('Programming'))
print('Machine Learning' in t)
print('---------------------------------')

for i in t:
    print(i)

print('---------------------------------')

t = (3, 1, 6, 13)

print(sum(t))
print(max(t))
print(min(t))
print(t.count(13))
print(t*3)
print()
print(tuple(reversed(t)))
print('---------------------------------')

t1 = (3, 6)
t2 = (6, 3)

print(t1 == t2)
print('---------------------------------')

t = (9, 13)
t = t + (1,)

print(t)
print('---------------------------------')

t = (9, 13)
x = list(t)
x.append(1)
t = tuple(x)

print(t)
print('---------------------------------')

t = (13, 30, 1, 9, 8, 6)
x = list(t)
x.remove(30)
t = tuple(x)

print(t)
print('---------------------------------')

t = (1, 6)
x, y = t

print('x =', x)
print('y =', y)
print('---------------------------------')

person = ('Man', 27, 'USA')
gender,_,x = person

print('gender =', gender)
print('age =', _)
print('country =', x)
print('---------------------------------')

t1 = (1, 9)
t2 = (6, 13)
x = zip(t1, t2)
y = list(x)

print(list(y))
print(y[1])
print(type(y[1]))
print('---------------------------------')

z = [(1, 6), (9, 13)]
uz = zip(*z)

print(list(uz))
print('---------------------------------')

l = [1, 6, 8, (3, 9, 100), 0, 13, (10, 99), 7, 69]
counter = 0
for i in l:
    if type(i) == tuple:
        counter += 1

print(counter)
print('---------------------------------')

l = [1, 6, 8, (3, 9, 100), 0, 13, (10, 99), 7, 69]
counter = 0
for i in l:
    if isinstance(i, tuple):
        counter += 1

print(counter)
print('---------------------------------')

l = [(9, 13, 1, 7), (6, 3, 8, 10)]
x = [i[:-1] + (0,) for i in l]

print(x)
