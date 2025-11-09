s = 'abcdefg'

print(s[2:4])
print(s[2:-1])
print(s[2:6])
print(s[::-1])
print('---------------------------------')

s = 'Washington'

print(len(s))
print(max(s))
print(min(s))
print('---------------------------------')

print(ord('W'))
print(ord('a'))
print(ord('s'))
print(ord('h'))
print(ord('i'))
print(ord('n'))
print(ord('g'))
print(ord('t'))
print(ord('o'))
print(ord('n'))
print('---------------------------------')

print(chr(87))
print(chr(97))
print('---------------------------------')

s = 'Business'

print('ss' in s)
print('ua' not in s)
print(s=='Business')
print(s < 'NewYork')
print(s.islower())
print(s.isupper())
print(s.isalnum())
print(s.isalpha())
print('---------------------------------')

s = 'Industry5'

print(s.isalnum())
print(s.isalpha())
print('---------------------------------')

s = '#Industry5'

print(s.isalnum())
print(s.isalpha())
print('---------------------------------')

s = '963'

print(s.isdigit())
print('---------------------------------')

print('\t'.isspace())
print('---------------------------------')

s = '9a6b3cde'
n = 0

for ch in s:
    if ch.isdigit() == True:
        n += int(ch)

print(n)
print('---------------------------------')

s = 'United States of America'

print(s.startswith('Am'))
print(s.endswith('ca'))
print(s.find('e'))
print(s.index('e'))

print(s.find('w'))
#print(s.index('w'))

print(s.find('e', 5))
print(s.find('e', 12))

print(s.count('e'))
print(s.count('e', 5))
print('---------------------------------')

s = 'AuthorSupport@elsevier.com'
f = s.find('@')

print(s[f+1:])
print('---------------------------------')

s = 'google and apple'

print(s.capitalize())
print(s.title())
print('---------------------------------')

s = 'GoOgle'

print(s.lower())
print(s.upper())
print(s.swapcase())
print('---------------------------------')

s = 'TimHoward'

print(s.replace('Howard', 'Cook'))
print('---------------------------------')

s = '$$apple$$$'

print(s.strip('$'))
print(s.lstrip('$'))
print(s.rstrip('$'))
print('---------------------------------')

s = '$$apple###'

print(s.lstrip('$').rstrip('#'))
print('---------------------------------')

s = 'www.google.com'

print(s.lstrip('www.'))
print('---------------------------------')

s = 'AI helps you be more productive.'
l = s.split(' ')

print(l)
print('---------------------------------')

l = ['AI', 'helps', 'you', 'be', 'more', 'productive.']
s = ' '.join(l)

print(s)
print('---------------------------------')

file = '03_strings.py'
f = file.split('.')

print(f)
print('---------------------------------')

s = 'zuckerberg@gmail.com'
u = s.split('@')

print(u)
print('---------------------------------')

s = 'mark\nzuckerberg'
l = s.split('\n')

print(l)
print('---------------------------------')

s = 'mark\nzuckerberg'
l = s.splitlines()

print(l)
print('---------------------------------')

s = '963.03.06.009'
n = [str(int(i)) for i in s.split('.')]
j = '.'.join(n)

print(j)
print('---------------------------------')

s = '13'

print(s.zfill(8))
print('---------------------------------')

s = 'Bill'

print(s.ljust(6, '+'))
print(s.rjust(6, '+'))
print(s.center(6,'+'))
print('---------------------------------')

year = 2026

print(f'Winner of the {year} FIFA World Cup.')
print('---------------------------------')

name = 'Mary'

print('name: {0}'.format(name))
print('---------------------------------')

fname = 'Mary'
lname = 'Mirzakhani'

print('name: {0} family: {1}'.format(fname, lname))
print('---------------------------------')

name = 'Mary'

print(f'name : {name}')
print(f'name : {name!r}')
print('---------------------------------')

n = 13

print('{0:d}'.format(n))
print('---------------------------------')

n = 13

print('{0:6d}'.format(n))
print('---------------------------------')

n = 13
m = 33

print('{0:f} {1:d}'.format(n, m))
print('---------------------------------')

n = 63.999

print('{:.2f}'.format(n))
print('---------------------------------')

n = 0.36

print('{:.2%}'.format(n))
print('---------------------------------')

n = 90000000

print('{:,}'.format(n))
print('---------------------------------')

n = 13

print('{:X}'.format(n))
print('{:#X}'.format(n))
print('---------------------------------')

n = 13

print('{:b}'.format(n))
print('{:#b}'.format(n))
print('---------------------------------')

n = 69

print('{:*>6d}'.format(n))
print('{:*<6d}'.format(n))
print('{:*^6d}'.format(n))
