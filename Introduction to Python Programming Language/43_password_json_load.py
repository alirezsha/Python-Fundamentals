import json

file_path = 'F:/Offline Courses/03 - Python/password.json'

with open(file_path) as f:
    password = json.load(f)
    print(f'Your password is: {password}')
