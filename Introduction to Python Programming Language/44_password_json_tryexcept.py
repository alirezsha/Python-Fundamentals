import json

file_path = 'password.json'

try:
    with open(file_path) as f:
        password = json.load(f)
except FileNotFoundError:
    password = input('Enter the password: ')
    with open(file_path, 'w') as f:
        json.dump(password, f)
        print(f'Password set by you: {password}')
else:
    print(f'Your password is: {password}')
