from unittest import mock
import faker


m = mock.Mock()
f = faker.Faker()

m.losowa_osoba = f.name()
m.losowa_sentencja = f.sentence()
m.losowa_data = f.date()

print(m.losowa_osoba, m.losowa_sentencja, m.losowa_data)