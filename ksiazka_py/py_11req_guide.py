import requests

r1 = requests.get('https://api.github.com/events')
print('r1', r1)
print(r1.headers)

r2 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print('r2', r2)
print(r2.json())

r3 = requests.put('https://httpbin.org/put', data={'key': 'value'})
r4 = requests.delete('https://httpbin.org/delete')
r5 = requests.head('https://httpbin.org/get')
r6 = requests.options('https://httpbin.org/get')

print('put', r3)
print(r3.json())
print('detele', r4)
print(r4.json())
print('head', r5)
print(r5.text)
print(r5.headers)
# print(r5.json())  # ex
print('options', r6)
print(r6.text)
print(r6.headers)
# print(r6.json())  # ex
print(r1.history)

r7 = requests.get('http://github.com/', allow_redirects=False)
print('r7', r7)
print(r7.history)

r8 = requests.get('http://github.com/', allow_redirects=True)
print('r8', r8)
print(r8.history)
print(r8.elapsed)

# za krótki timeout i dostaniemy except
# 'Connection to github.com timed out. (connect timeout=0.001)'
# r9 = requests.get('http://github.com/', timeout=0.001)