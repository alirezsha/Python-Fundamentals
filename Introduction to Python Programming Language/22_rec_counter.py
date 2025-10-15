def counter(a):
    if a <= 0:
        print('End')
    else:
        print(a)
        counter(a-1)
        