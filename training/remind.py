# get ASCII chars

l1 = list()
for i in range(97, 108):
    l1.append(chr(i))
l1

# by list comprehension
l1 = [chr(i) for i in range(97, 108)]
l1

# deleting a slice from list
l1

l1[3:8]
del l1[3:8]
l1

# sort and reverse
l1.reverse()
l1
l1[::-1]  # reverse by slice

# sets
s1 = set([chr(i) for i in range(97, 108, 2)])
s1
s2 = set([chr(i) for i in range(97, 108)]) - s1
s2
s2.update(['a', 'c'])
s2
s2.intersection(s1)
s2.issubset(s1)
s2.union(s1)
s2.difference(s1)
s2.difference_update(s1)
s2
s2 = set([chr(i) for i in range(97, 108)]) - s1
s2.update(['a', 'c'])
s2
s2.symmetric_difference(s1)
s2.isdisjoint(s1)
s2.isdisjoint({'y', 'z'})
s2.issuperset({'a', 'b', 'c'})

import functools
import time
# LRU
from datetime import datetime


@functools.lru_cache(maxsize=None)
def czek_lru():
    time.sleep(1)
    return 1


def czek():
    time.sleep(1)
    return 1


start = datetime.now()
for _ in range(2):
    czek_lru()
elapsed = datetime.now() - start
print('czek_lru():\t' + str(elapsed))

start = datetime.now()
for _ in range(2):
    czek()
elapsed = datetime.now() - start
print('czek():\t' + str(elapsed))


# pandas
import os

cur_dir = os.getcwd()
cur_dir
airtravel = 'files_sources/airtravel.csv'
if cur_dir != 'D:\\Mateusz\\nauka\\python\\hello':
    airtravel = '../' + airtravel
airtravel

import pandas as pd

df = pd.read_csv(airtravel)
df.head(1)
df.columns = ['Month', 1958, 1959, 1960]
df.tail(1)
df.iloc[0]
df.iloc[-1]
df.shape
df.size
df.shape[0] * df.shape[1]


# generators
def get_row_by_row(df: pd.DataFrame):
    for i in range(len(df)):
        yield df.iloc[i]


at2 = pd.DataFrame()
for row in get_row_by_row(df):
    at2 = at2.append(row)
at2
at2 = pd.DataFrame()
at_gen = get_row_by_row(df)
next(at_gen)


# decorators
def decor(func):
    print('before')

    def internal_f(x):
        x = x.lower()
        print('internal before')
        func(x)
        print('internal after')

    print('after')
    return internal_f


def print_name(name: str):
    print(name.swapcase())


@decor
def print_name_decor(name: str):
    print(name.swapcase())


print_name('Jarek')

print_name_decor('Jarek')

# os
import os

os.getcwd()
dirs = os.walk(os.getcwd())
next(dirs)
os.listdir()
os.path.exists('../files_sources/')
os.path.exists('files_sources/')
os.path.isdir('../files_sources/')
os.path.isdir('files_sources/')
os.path.isfile('files_sources/')
os.path.getsize(airtravel)
# mkdir, rmdir, remove...


# subprocess
import subprocess

result = subprocess.call(['ping', '-n', '2', 'onet.pl'])
result  # if ok returns 0, if an error returns 1
result = subprocess.Popen(['ping', '-n', '2', 'onet.pl'])
result.communicate()

# faker lib
import faker

f = faker.Faker()
f.name()
f.sentence()
f.date()
f.time()
f.future_datetime()
f.word()
f.email()
f.free_email()
f.free_email_domain()
f.name_male()
f.name_female()
f.first_name_female()
f.firefox()
f.first_name_nonbinary()
f.fixed_width()

f.__dict__

f.locales
f.seed_locale('en_US')
f.factories.insert(2, 2)
f.factories.pop()
f.random.randrange(20)

# plots
# common linear plots
from matplotlib import pyplot as plt

plt.style.use('dark_background')
df.plot(grid=True)
df

df.iloc[:, 1]

plt.plot(df.iloc[:, 1], '-', label='1958')
plt.plot(df.iloc[:, 2], '--')
plt.plot(df.iloc[:, 3], ':')

plt.xlabel('Month')
plt.ylabel('count')
plt.grid()
df.columns[1:]
df.columns[:0:-1]
plt.legend(df.columns[1:])

# todo bar/hist plots; page 161
df.iloc[:, 1:].values

plt.bar(df.iloc[:, 0], df.iloc[:, 1])
plt.bar(df.iloc[:, 0], df.iloc[:, 2])
(plt.bar(df.iloc[:, 0], df.iloc[:, 3]))[6].set_color('r')


plt.bar(df.iloc[:, 0], df.iloc[:, 1], label=1958)
plt.plot(df.iloc[:, 3], 'b--', label=1960)
plt.legend()


# iterators
class IncrementIter:
    def __init__(self, n: int):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.i:
            raise StopIteration
        else:
            self.i += 1
            return self.i


it1 = IncrementIter(5)
for i in IncrementIter(4):
    print(i)

next(it1)

# Generator jest funkcją która może zostać wstrzymana i wznowiona od miejsca,
# w którym została. Generatory cechują się leniwą ewaluacją. [yield]

# Iterator to obiekt pozwalający na sekwencyjny dostęp do kolejnych elementów.
# Aby stworzyć iterator w klasie zaimplementować dwie funkcje:
# `__iter__()` i `__next__()`
