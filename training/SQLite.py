import sqlite3

with sqlite3.connect('../files_sources/northwind.db') as connection:
    connection.text_factory = lambda b: b.decode(errors='ignore')
    # rows = connection.execute('select * from Customers')
    # print(next(rows))
    # print(next(rows))
    # connection.execute(
    #     'insert into Customers values'
    #     '("DALAJ", "dalajlama", "Dalaj", "Owner", "ul. Miła 2", "Kielce", "PL", "25437", "Poland",'
    #     '"+48 500 500 500", "+48 22 247 22 49")')
    # connection.commit()
    insert1 = "INSERT INTO Categories (CategoryName) VALUES ('test');"
    select1 = "SELECT CategoryId, CategoryName FROM Categories c;"
    update1 = "UPDATE Categories SET CategoryName = 'new test' WHERE CategoryID = 9;"
    update2 = "UPDATE Categories SET CategoryName = 'new test2' WHERE CategoryID >= 9;"
    delete1 = "DELETE FROM Categories WHERE CategoryID = 9;"
    delete2 = "DELETE FROM Categories WHERE CategoryID >= 9;"
    cursor = connection.cursor()

    def prods():
        cursor.row_factory = sqlite3.Row
        p = cursor.execute(select1).fetchall()
        for row in p:
            print(dict(row))
    # l1 = [('Russian', 5), ('English', 10), ('Polish', 30)]
    # cursor.execute("create table lang (lang_name, lang_age)")
    # cursor.close()
