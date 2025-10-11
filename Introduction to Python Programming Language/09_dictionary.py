import pprint

candidates = {}

candidates['Alireza'] = {'Name': 'Alireza Sh',
                         'Gender': 'Male',
                         'Field': 'Data Science and Industrial Eng.',
                         'Born': '1997-Tehran'}

candidates['Amir'] = {'Name': 'Amir Sh',
                         'Gender': 'Male',
                         'Field': 'Industrial Engineering and Optimization',
                         'Born': '1991-Tehran'}

candidates['Maryam'] = {'Name': 'Maryam Mirzakhani',
                         'Gender': 'Female',
                         'Field': 'Mathematical',
                         'Born': '1977-Tehran'}

candidates['Donald'] = {'Name': 'Donald Trump',
                         'Gender': 'Male',
                         'Field': 'Business',
                         'Born': '1946-New York'}

print(candidates['Amir'])
#print(candidates['Maryam']['Field'])
#print(candidates)
#pprint.pprint(candidates)