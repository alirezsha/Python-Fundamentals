file_path = 'F:/Offline Courses/03 - Python/data_1.txt'

# with open(file_path) as f:
#     for line in f:
#         print(line)

with open(file_path) as f:
    lines = f.readlines()
for line in lines:
    print(line)
