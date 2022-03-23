import requests
from bs4 import BeautifulSoup as bs
from IPython.display import Image

# GET
response = requests.get('https://httpbin.org/ip')
print('response', response)
print(response.json())
print(response.content)
print(type(response.content))

# GET SOUP
soup = bs(requests.get('https://onet.pl').text, 'html.parser')
print(soup.title)
print(soup.title.text)
print(soup.title.parent.name)

req2 = requests.get('https://httpbin.org/get?param1=HELLO&other_param=12345')
print('req2', req2)
print(req2.json())
print(req2.json()['args'])

req3 = requests.get(
    'https://httpbin.org/get',
    params={
        'param1': 'HELLO',
        'other_param': 12345
    }
)
print('req3', req3)
print(req3.json())
print(req3.json()['args'])

par4 = {
    'a': [1, 2, 3],
    'b': 2
}
req4 = requests.get('https://httpbin.org/get', params=par4)
print('req4', req4)
print(req4.json())
print(req4.json()['args'])

req5 = requests.get(
    'https://api.thecatapi.com/v1/images/search',
    params={'format': 'json', 'order': 'RANDOM', 'limit': 1}
)
print('req5', req5)
print(req5.json())
url5 = req5.json()[0]['url']
print(Image(requests.get(url5).content))

req6 = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/gbp/last/10/',
                    params={'format': 'json'})
print('req6', req6)
print(req6.json())
print(req6.json()['rates'])
for rate in req6.json()['rates']:
    print(rate)

# POST
post_data = {
    'param_1': 'HI!',
    'other_param': 12345
}
req7 = requests.post('https://httpbin.org/post', data=post_data)
print('req7', req7)
print(req7.json())

req8 = requests.post('https://httpbin.org/post', json=post_data)
print('req8', req8)
print(req8.json())

req8 = requests.post(
    'https://httpbin.org/post', data=post_data,
    headers={'Content-Type': 'application/json'}
)
print('req8', req8)
print(req8.json())

# autentykacja
req9 = requests.get('https://httpbin.org/basic-auth/daftacademy/bardzosilnehaslo')
print('req9', req9)  # 401
# print(req9.json())

req10 = requests.get(
    'https://httpbin.org/basic-auth/daftacademy/bardzosilnehaslo',
    auth=('daftacademy', 'bardzosilnehaslo')
)
print('req10', req10)
print(req10.status_code)
print(req10.json())

# sesje
s1 = requests.Session()
print('s1', s1)
print(type(s1))
s1.headers.update({'__x-test': 'true'})
print('s1.headers', s1.headers)
sg1 = s1.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print('sg1', sg1)
print(sg1.json())
# zapamiętane cookie
req11 = s1.get('https://httpbin.org/cookies')
print('req11', req11)
print(req11.json())
print(req11.text)
print(req11.request)
print(req11.request.url)
print(req11.request.headers)
print(req11.request.body)
print(req11.request.hooks)
print(req11.request.method)
