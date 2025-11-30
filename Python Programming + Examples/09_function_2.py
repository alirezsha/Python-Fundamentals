def reverse(s):
    output = ''.join(reversed(s))
    return output

print(reverse('Intelligence'))
print()
print(reversed('Intelligence'))
print()
print(list(reversed('Intelligence')))
print('---------------------------------')

s = 'refer' #'tenet' #'racecar' #'level'
def palindrome(s):
    return s == s[::-1]

print(palindrome(s))
print()
print(palindrome('NewYork'))
print('---------------------------------')

s = 'Artificial'
def remove_ch(s, start, end):
    if len(s) > end:
        s = s[0: start] + s[end+1 ::]
    return s

print(remove_ch(s, 3, 6))
print('---------------------------------')

s = 'Artifical'
def remove_oddchar(s):
    output = ''
    for ch in range(len(s)):
        if ch % 2 == 0:
            output += s[ch]
    return output

print(remove_oddchar(s))
print('---------------------------------')

l = [6, 9, 7, 13, 3, 9]
def remove_dup(l):
    output = []
    for i in l:
        if i not in output:
            output.append(i)
    return output

print(remove_dup(l))
print('---------------------------------')

def func(n):
    output = [1]
    for i in range(2, n):
        if (n % i) == 0:
            output.append(i)
    return output

l = func(33)
print(l)
print('---------------------------------')

s = 'AI helps you be more productive '
def long_wrd(s):
    word = ''
    l = []
    for ch in range(0, len(s)):
        if (s[ch] != ' '):
            word += s[ch]
        else:
            l.append(word)
            word = ''
    m = l[0]
    for i in range(0, len(l)):
        if (len(l[i]) > len(m)):
            m = l[i]
    return m

print(long_wrd(s))
print('---------------------------------')

def pascal_tri(n):
    a = [1]
    b = [0]
    for i in range(max(n, 0)):
        print(a)
        a = [x+y for x,y in zip(a+b, b+a)]

pascal_tri(10)
print('---------------------------------')

l = [6, 9, 7, 13, 3, 9]
def remove_dup(l):
    return list(set(l))

print(remove_dup(l))
print('---------------------------------')

s = 'george mary peter mark george peter bill'
def func(s):
    set1 = set()
    word = s.split()
    for w in word:
        if w in set1:
            return w
        else:
            set1.add(w)
    return 'None'

print(func(s))
print('---------------------------------')

n = 99
def prime(n):
    l = []
    prime_set = set()
    for i in range(2, n+1):
        if i in prime_set:
            continue
        for j in range(i*2, n+1, i):
            prime_set.add(j)
        l.append(i)
    return l

print(prime(n))
print('---------------------------------')

matrix = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]
def magic_square(m):
    n = len(m[0])
    l = []
    
    l.extend([sum(i) for i in m])
    
    for col in range(n):
        l.append(sum(row[col] for row in m))
    
    output1 = 0
    for i in range(0, n):
        output1 += m[i][i]
        
    l.append(output1)
        
    output2 = 0
    for i in range(0, n):
        output2 += m[i][2-i]
        
    l.append(output2)
    
    if len(set(l)) > 1:
        return False
    else:
        return True

print(magic_square(matrix))
