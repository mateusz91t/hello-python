import requests

try:
    r1 = requests.get('http://jsystems.pl/static/blog/python/dane.json',
                      auth=('user', 'pass')
                      )
    print('r1', r1)
    print(r1.status_code)
    print(type(r1.json()), r1.json())
    print(type(r1.text), r1.text)
    print(r1.json()['adres']['kod'])
    print(r1.url)
    print(r1.headers)
    print(r1.cookies)
    print(r1.elapsed)
    print(r1.history)
    print(r1.reason)
    print(r1.apparent_encoding)
    r1.close()
    print('r1', r1)
except Exception as ex:
    pass

dane = dict()
r2 = \
    requests.post("http://jsystems.pl/static/blog/python/dane.json",
                  data=dane,
                  headers={"Content-Type": "application/json"})
print('r2', r2.status_code)
