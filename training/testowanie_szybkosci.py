import timeit

db_avg = timeit.timeit(
    "v1 = csr.execute('select avg(unitprice) from products').fetchone()",
    setup="import sqlite3; con = sqlite3.connect('../files_sources/northwind.db'); csr = con.cursor()",
    number=100000
)

py_avg = timeit.timeit(
    "v1 = csr.execute('select unitprice from products').fetchall(); l = [x[0] for x in v1]; sum(l)/len(l)",
    setup="import sqlite3; con = sqlite3.connect('../files_sources/northwind.db'); csr = con.cursor()",
    number=100000
)

print(f"db_avg = {db_avg}\npy_avg = {py_avg}")
print(f"db_avg - db_avg = {abs(db_avg - py_avg)}")


# list vs tuple
lt = timeit.timeit(
    'l1 = list(random.randint(0, len(l)) for _ in l)',
    setup='import random; l = list(x for x in range(1000000))',
    number=10
)
tt = timeit.timeit(
    't1 = tuple(random.randint(0, len(t)) for _ in t)',
    setup='import random; t = tuple(x for x in range(1000000))',
    number=10
)

print(f"list = {lt}")
print(f"tuple = {tt}")


# output in CPython:
# db_avg = 17.7117786
# py_avg = 22.7901368
# db_avg - db_avg = 5.0783582
# list = 11.382604700000002
# tuple = 11.870016

# output in PyPy:
# db_avg = 17.4833119
# py_avg = 20.7942641
# db_avg - db_avg = 3.310952199999999
# list = 1.8074535999999952    !!!
# tuple = 2.548409499999998    !!!
