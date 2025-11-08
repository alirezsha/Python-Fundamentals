for i in range(6):
    print(i)
    
print('---------------------------------')

for j in range(6):
    print(j, end=' ')
    
print('---------------------------------')

for i in range(3, 13):
    print(i, end=' ')

print('---------------------------------')

for i in range(3, 13, 3):
    print(i, end=' ')

print('---------------------------------')

# name = input("Enter the name: ")
name = 'Maryam Mirzakhani'
for ch in name:
    print(ch)

print('---------------------------------')

for _ in range(6):
    print('USA')

print('---------------------------------')

for i in range(13, 3, -3):
    print(i, end=' ')
    
print('---------------------------------')

# string = input("Enter the string: ")
string = 'Viva America'
count = 0

for ch in string:
    count += 1

print(count)
print('---------------------------------')

# string = input("Enter the string: ")
string = 'Viva America'
count = 0

for ch in string:
    if ch == 'A':
        count += 1

print(count)
print('---------------------------------')

# phrase = input("Enter the phrase: ")
phrase = 'United States of America'
vowels = 'AaEeIiOoUu'
count = 0

for ch in phrase:
    if ch in vowels:
        print(ch, end=' ')
        count += 1

print('\n', count)
print('---------------------------------')

# phrase = input("Enter the phrase: ")
phrase = 'United States of America'
vowels = 'AaEeIiOoUu'

char = [ch for ch in phrase if ch in vowels]

print(char)
print('---------------------------------')

for i in range(3, 6):
    for j in range(6, 9):
        print(j, end=' ')
    print()
    
print('---------------------------------')

for i in range(3, 6):
    for j in range(6, 9):
        print(i, end=' ')
    print()

print('---------------------------------')

for i in range(6):
    for j in range(i):
        print(j, end=' ')
    print()

print('---------------------------------')

for i in range(2, 6):
    for j in range(1, i):
        print(j, end=' ')
    print()

print('---------------------------------')

for i in range(6):
    if i == 5:
        break
    else:
        print(i, end=' ')
    
print('---------------------------------')

for i in range(9):
    if i == 6:
        continue
    else:
        print(i, end=' ')

print('---------------------------------')

for i in range(6, 13):
    for j in range(3, i):
        if i % j == 0:
            print(i, end=' ')
            break

print('---------------------------------')

for i in range(3, 30):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')

print('---------------------------------')

a = 3
while a <= 6:
    print(a, end=' ')
    a += 1

print('---------------------------------')

x = 9
while x >= 6:
    print(x, end=' ')
    x -= 1

print('---------------------------------')

# string = input("Enter the string: ")
string = 'Viva America'
c = 0

while True:
    if string[c] == 'A':
        break
    print(string[c], end='')
    c += 1

print('\n---------------------------------')

x = 9

while x > 3:
    x -= 1
    if x == 6:
        break
    print(x, end=' ')
    
print('\n---------------------------------')

x = 9

while x > 3:
    x -= 1
    if x == 6:
        continue
    print(x, end=' ')
    
print('---------------------------------')

x = 0
y = 1

while x < 99:
    print(x, end=' ')
    x = y
    y = y + x

print('---------------------------------')

x = 0
y = 1

while x < 99:
    print(x, end=' ')
    x, y = y, y + x
    
print('---------------------------------')

import random

x = random.randrange(0, 99)

flag = 'No'

while flag == 'No':
    y = int(input("Enter a number: "))
    if y < x:
        print('Increase the number you guessed.')
    elif y > x:
        print('Reduce the number you guessed.')
    else:
        print("It's correct.")
        flag = 'Yes'

print('Thank you for your time.')
