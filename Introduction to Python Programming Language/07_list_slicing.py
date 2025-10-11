#'!hello good morning ,' to 'modeling'

phrase = '!hello good morning ,'
phrase_list = list(phrase)

print(phrase)
print(phrase_list)

print('------------------------')

# first step
new_phrase = ''.join(phrase_list[-9:-7])

# second step
new_phrase = new_phrase + ''.join([phrase_list[10], phrase_list[2],
                                  phrase_list[3], phrase_list[-5],
                                  phrase_list[-4], phrase_list[-3]])

new_phrase_list = list(new_phrase)

print(new_phrase)
#print(phrase_list)
print(new_phrase_list)
