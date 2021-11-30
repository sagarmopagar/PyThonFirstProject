# with open('test.txt', 'r') as f:
#     file = f.read(3)
#     while (file):
#         print(file, end='')
#         file = f.read(3)
#
#
# print('\n\n')
# import re
# Movies = ['The final destination',
#          'The American Story',
#          'Gone with the wind',
#          'In the final hour',
#          'A man in the final room']
#
# for movie in Movies:
#     print('Movie name: ',movie)
#     # movie = '/usr/home:lumberjack'
#     matches = re.match('[.*](.*)The final[.*](.*)', movie)
#     result = matches.groups()
#     print(result)


## FILE HANDLING ###
from faker import Faker
fake = Faker('it_IT')

with open('data.txt', 'w') as f:
    for i in range(100):
        f.write(fake.name()+'\n')

# Read File Operation
with open('data.txt', 'r') as f:
# line = f.read(100)
# while(line):
#     print(line.rstrip())
#     line = f.read(100)
    for line in f:
        print(line.rstrip(),end='')