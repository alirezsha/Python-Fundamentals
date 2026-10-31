def factorial(n):
    if not isinstance(n, int):
        print('factorial only applies to integers!')
        return None
    elif n < 0:
        print('factorial only applies to positive numbers!')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
