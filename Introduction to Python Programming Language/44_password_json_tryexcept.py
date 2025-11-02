import json

file_path = 'F:/Offline Courses/03 - Python/password.json'

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
