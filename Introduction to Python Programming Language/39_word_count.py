def word_count(file_path):
    try:
        with open(file_path) as f:
            contents = f.read()
    except FileNotFoundError:
        print('The file does not exist.')
        #pass
    else:
        words = contents.split()
        number_of_words = len(words)
        print(f'file {file_path} has {number_of_words} words.')

file_path = ['a.txt',
             'data_1.txt',
             'data_2w.txt']
for file in file_path:
    word_count(file)


