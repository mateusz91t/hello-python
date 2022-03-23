import collections
import random
import re
import typing
from faker import Faker
from operator import itemgetter


# ============== Counter & Faker =============
random.seed(3)
l = [random.randint(0, 10) for x in range(10)]
l
collections.Counter(l)

f = Faker('pl_PL')
Faker.seed(1)
dir(f)
sen = f.sentence()
sen
list(sen)
counted = collections.Counter(sen)
counted
sorted(list(counted.items()), key=itemgetter(1), reverse=True)

# =============== ChainMap =================
f = Faker('pl_PL')

def get_names(how_many: int = 10):
    return [re.split(' ', f.name(), maxsplit=1) for x in range(how_many)]
names1, names2 = get_names(), get_names()
d1, d2 = dict(names1), dict(names2)
d1
d2
cm = coll.ChainMap({}, d1, d2)
cm
cm['pan']
cm.setdefault(key=str, default='BRAK')
cm.get('panaaaaaaa', 'BRAK')
cm.maps[0].clear()
cm['Borys']


typing.Counter(l)
collections.Counter(l)