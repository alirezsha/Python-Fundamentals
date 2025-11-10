l = [3, 5, 7, 9]

print(type(l))
print(len(l))
print('---------------------------------')

l = [13, 15, 17, 19]

print(l.index(13))
print(l[0])
print('---------------------------------')

s = 'University'

print(s[3])
print('---------------------------------')

team = ['Mary', 'Albert', 'Donald']
for p in team:
    print(p)

print('---------------------------------')

team = ['Mary', 'Albert', 'Donald']
for p in range(3):
    print(team[p])
    
print('---------------------------------')

l = [9, 13, 30, 1, 96, 60, 100, 7]

print(l[3:6])
print(l[:6])
print(l[2:])
print(l[6:0])
print(l[::-1])
print(l[1:6:2])
print(l[7:1:-2])

l[1:3] = [700, 600]

print(l)
print('---------------------------------')

l = [10, 30]
x = l*3

print(x)
print('---------------------------------')

l = [10, 30]
i = ['x', 'y', 'z']
m = l + i

print(m)
print('---------------------------------')

l = [10, 30, 100]

print(1 in l)
print(1 not in l)
print('---------------------------------')

l = [9, 6, [7, 8, 9], 13, 69]

print(l[2])
print(l[2][0])
print('---------------------------------')

l = [13, 11, 12, 100, 36, 33]
i = -1
for n in l:
    if n > i:
        i = n

print(i)
print('---------------------------------')

l = [13, 11, 12, 100, 36, 33]
i = 0
for n in l:
    i += n

print(i)
print('---------------------------------')

l = [3, 6, 9, 3, 1]

print(l.count(3))
print('---------------------------------')

l = [3, 6, 9, 3, 1]
l.insert(1, 2)

print(l)
print('---------------------------------')

l = [3, 6, 9, 3, 1]
l.remove(3)

print(l)
print('---------------------------------')

l = [10, 20, 30, 60]
l.pop()

print(l)
print('---------------------------------')

l = [10, 20, 30, 60]
a = l.pop()

print(a)
print('---------------------------------')

l = ['x', 'y', 'z']
a = l.pop(1)

print(l)
print(a)
print('---------------------------------')

l = [1, 2, 3]
del l[1]

print(l)
print('---------------------------------')

l = [10, 20, 30, 40, 50, 60]
del l[3:5]

print(l)
print('---------------------------------')

l = [10, 20, 30, 40, 50, 60]
l.reverse()

print(l)
print('---------------------------------')

l = [10, 20, 30, 40, 50, 60]

print(l[::-1])
print('---------------------------------')

l = [90, 30, 60, 20, 10, 40]
l.sort()

print(l)
print('---------------------------------')

a = [10, 20, 30]
b = [90, 60, 1]
a.extend(b)

print(a)
print('---------------------------------')

a = [10, 20, 30]
b = [90, 60, 1]
b.extend(a)

print(b)
print('---------------------------------')

a = [10, 20, 30]
b = [90, 60, 1]
a.append(b)

print(a)
print('---------------------------------')

l = [10, 20, 30]
l.append(60)

print(l)
print('---------------------------------')

l = [10, 20, 30]
l.clear()

print(l)
print(len(l))
print('---------------------------------')

l = [10, 20, 30]
x = l.copy()

print(x)
print('---------------------------------')

l = []
for i in range(6):
    l.append(i)
    
print(l)
print('---------------------------------')

l = [i for i in range(6)]

print(l)
print('---------------------------------')

l = [i*2 for i in range(6)]

print(l)
print('---------------------------------')

l = [i**2 for i in [3, 4, 5]]

print(l)
print('---------------------------------')

l = [i*i for i in range(3, 6)]

print(l)
print('---------------------------------')

l = [10, -30, 3, 6.5, -99]
x = [abs(i) for i in l]

print(x)
print('---------------------------------')

import math
l = [round(math.pi, i) for i in range(1, 6)]

print(l)
print('---------------------------------')

l = ['#Albert', 'Mary#']
x = [i.strip('#') for i in l]

print(x)
print('---------------------------------')

l = [19, 18.3, 20, 9, 6, 16.3]
x = [i for i in l if i > 15]

print(x)
print('---------------------------------')

l = [30, 10]
x = [60, 10, 100, 1]
y = []
for i in l:
    for j in x:
        y.append((i, j))
        
print(y)
print('---------------------------------')

l = [30, 10]
x = [60, 10, 100, 1]
y = []
for i in l:
    for j in x:
        if i != j:
            y.append((i, j))
        
print(y)
print('---------------------------------')

l = [float('Nan'), 3.14, 6.5, float('NaN'), 1.3]
x = []

import math

for i in l:
    if not math.isnan(i):
        x.append(i)
        
print(x)
print('---------------------------------')

m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

print(len(m))
print(m[3])
print('---------------------------------')

m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
for i in m:
    print(i)

for i in m:
    print(i[1], end=' ')
print()

for i in range(0, 4):
    print(m[i][i], end=' ')
print()

for i in range(0, 4):
    print(m[i][3-i], end=' ')
print()

row = []
row.extend([sum(i) for i in m])

print(row)
print()

column = []
for c in range(4):
    column.append(sum(i[c] for i in m))
    
print(column)
print('---------------------------------')

a = 3
b = a
b += 1

print(a)
print(b)
print()

l1 = []
l2 = l1
l2.append(6)

print(l1)
print(l2)
