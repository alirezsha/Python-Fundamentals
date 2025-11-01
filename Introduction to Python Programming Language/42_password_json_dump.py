import json

password = input('Enter the password: ')

file_path = 'password.json'

with open(file_path, 'w') as f:
    json.dump(password, f)
    print(f'Password set by you: {password}')
