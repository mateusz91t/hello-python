import imp
import psycopg2
from x_data import postgre_sql_pass

# połączenie i select
polaczenie = psycopg2.connect(
    host='localhost', database='postgres', user='postgres', password=postgre_sql_pass
)
print('polaczenie', polaczenie)
print(type(polaczenie))
kursor = polaczenie.cursor()
print('kursor', kursor)
print(type(kursor))
kursor.execute('select * from owoce')
for wiersz in kursor:
    print(wiersz, '\t', type(wiersz), wiersz[0], wiersz[1])  # tuple

# insert
# returning numer - zwraca to co DB generuje automatycznie w kolumnie numer
kursor.execute("insert into owoce (nazwa) values ('mandarynka') returning numer")
kf1 = kursor.fetchone()  # fetch wykorzystuje zapisane w kursorze
print('kursor.fetchone()', kf1)
print(type(kf1))
print('kursor.fetchone()[0]', kf1[0])
print(type(kf1[0]))
polaczenie.commit()
kursor.close()
