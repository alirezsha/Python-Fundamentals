import json

file_path = 'F:/Offline Courses/03 - Python/numbers.json'

with open(file_path) as f:
    numbers = json.load(f)

print(numbers)
