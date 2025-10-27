print('Enter two numbers to divide.')
print('Exit the program by entering q.')

while True:
    first_number = input('\nfirst_number: ')
    if first_number == 'q':
        break
    second_number = input('\nsecond_number: ')
    if second_number == 'q':
        break
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('It is impossible to divide a number by zero.')
    else:
        print('\n', result)
