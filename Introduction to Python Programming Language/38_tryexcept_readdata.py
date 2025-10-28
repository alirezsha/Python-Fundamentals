file_path = 'F:/Offline Courses/03 - Python/data_1.txt'

try:
    with open(file_path) as f:
        contents = f.read()
except FileNotFoundError:
    print('The file does not exist.')
else:
    words = contents.split()
    number_of_words = len(words)
    print(f'file {file_path} has {number_of_words} words.')
