import json

file_path = 'numbers.json'

with open(file_path) as f:
    numbers = json.load(f)

print(numbers)
