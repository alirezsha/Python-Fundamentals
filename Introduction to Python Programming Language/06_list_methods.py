#'!hello good morning ,' to 'modeling'

phrase = '!hello good morning ,'
phrase_list = list(phrase)

print(phrase)
print(phrase_list)

print('------------------------')

# first step
for i in range(2):
    phrase_list.pop()

# second step
phrase_list.pop(0)

# third step
phrase_list.remove('h')
phrase_list.remove(' ')

# forth step
phrase_list.insert(0, phrase_list.pop(9))
phrase_list.insert(1, phrase_list.pop(4))
phrase_list.insert(2, phrase_list.pop(8))

# fifth step
phrase_list.remove('l')

# sixth step
phrase_list.insert(5, phrase_list.pop(12))

# seventh step
phrase_list.insert(6, phrase_list.pop(12))

# eighth step
for i in range(7):
    phrase_list.pop()

new_phrase = ''.join(phrase_list)

print(new_phrase)
print(phrase_list)
