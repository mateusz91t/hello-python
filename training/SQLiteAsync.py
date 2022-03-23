import aiosqlite


async def startup():
    connection = await aiosqlite.connect('../files_sources/northwind.db')
    connection.text_factory = lambda b: b.decode(errors="ignore")
    return connection

con = await startup()

# csr = con.execute("select * from categories")
# print(csr)

# con.close()
