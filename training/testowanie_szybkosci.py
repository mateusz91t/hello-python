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

print(f"{db_avg = }\n{py_avg = }")
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


# output:
# db_avg = 6.0632881
# py_avg = 12.784954099999998
# db_avg - db_avg = 6.721665999999998
# list = 11.344587
# tuple = 11.275824500000006
