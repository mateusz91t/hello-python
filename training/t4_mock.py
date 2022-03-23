import random
from unittest import mock
from datetime import datetime


for i in range(5):
    print(random.random())

with mock.patch('random.random') as mrandom:
    print('RANDOM MOCKED:\n')
    mrandom.return_value = 0.123
    for i in range(5):
        print(random.random())


datetime.now()

# cannot mock datetime.now() !!!
# with mock.patch('datetime.now()') as mnow:
#     mnow.return_value = datetime(2000, 1, 1)
#     print(datetime.now())
