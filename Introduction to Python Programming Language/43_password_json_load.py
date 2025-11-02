import json

file_path = 'password.json'

with open(file_path) as f:
    password = json.load(f)
    print(f'Your password is: {password}')
