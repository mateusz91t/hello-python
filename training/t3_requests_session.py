import requests as r


# Session().get zapamięta headersy jakie wysyłamy do serwera
# oraz cookies jakie otrzymamy od serwera
s = r.Session()

s.headers.update({'x-my-header': 'my-header-value'})
response = s.get('https://httpbin.org/cookies')
response = s.get('https://httpbin.org/cookies/set/c1/0123')
response
response.text


res2 = r.get('https://httpbin.org/cookies/set/c2/cII')
res2 = r.get('https://httpbin.org/cookies')
res2.text
