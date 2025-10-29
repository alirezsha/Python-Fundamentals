import json

numbers = [13, 33, 36, 39, 66, 63, 99]

file_path = 'numbers.json'

with open(file_path, 'w') as f:
    json.dump(numbers, f)
