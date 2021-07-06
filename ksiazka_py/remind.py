# get ASCII chars
l1 = list()
for i in range(97, 108):
    l1.append(chr(i))
l1

# by list comprehension
l1 = [chr(i) for i in range(97, 108)]
l1

# deleting a slice from list
print(l1)
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
s2.discard(s1)
s2
s1.discard(s2)
s1
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

# LRU
from datetime import datetime
import time
import functools

@functools.lru_cache(maxsize=None)
def czek_lru():
    time.sleep(1)
    return 1


def czek():
    time.sleep(1)
    return 1


start = datetime.now()
for _ in range(5):
    czek_lru()
elapsed = datetime.now() - start
print('czek_lru():\t' + str(elapsed))

start = datetime.now()
for _ in range(5):
    czek()
elapsed = datetime.now() - start
print('czek():\t' + str(elapsed))


#
import os
os.getcwd()

import pandas as pd
df = pd.read_csv('files_sources/airtravel.csv')
df.head(1)
df.tail(1)
df.iloc[0]
df.iloc[-1]
df.shape
df.size
df.shape[0] * df.shape[1]


def get_row_by_row(df:pd.DataFrame):
    for i in range(len(df)):
        yield df.iloc[i]

at2 = pd.DataFrame()
for row in get_row_by_row(df):
    at2 = at2.append(row)
at2
at2 = pd.DataFrame()
at_gen = get_row_by_row(df)
next(at_gen)
