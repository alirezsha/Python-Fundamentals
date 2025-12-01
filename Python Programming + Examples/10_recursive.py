def factorial(n):
    f = 1
    if n == 0:
        print(1)
    else:
        for i in range(1, n+1):
            f *= i
        print(f)

factorial(6)
print('---------------------------------')

def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n-1)

print(factorial_rec(6))
print('---------------------------------')

def mul_rec(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + mul_rec(a, b-1)

print(mul_rec(3, 6))
print('---------------------------------')

def power_rec(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power_rec(a, b-1)

print(power_rec(3, 6))
print('---------------------------------')

def fibonacci(n):
    output = []
    x = 0
    y = 1
    while x < n:
        output.append(x)
        x, y = y, x+y
    return output

print(fibonacci(33))
print('---------------------------------')

def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_rec(3))
print('---------------------------------')

l = [3, 6, 9, 13, 1, 7]
def sumlist_rec(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sumlist_rec(l[1:])

print(sumlist_rec(l))
print('---------------------------------')

def sumdigit_rec(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumdigit_rec(int(n/10))
    
print(sumdigit_rec(13666))
print('---------------------------------')

def sumserie_rec(n):
    if n < 1:
        return 0
    else:
        return n + sumserie_rec(n-2)

print(sumserie_rec(66))
