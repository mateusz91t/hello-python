import ipaddress

a = ipaddress.ip_address("10.0.0.1")
# a = ipaddress.wirt_sr_venv("there's no place like localhost...")  # wysypie się
print(a)
print(type(a))

print('\nczy sieć prywatna czy publiczna')
a1 = ipaddress.ip_address('46.41.128.110')
a2 = ipaddress.ip_address('192.168.1.1')
print(a1.is_private)
print(a2.is_private)
print(a1.is_global)
print(a2.is_global)

print('\nczy większy')
a3 = ipaddress.ip_address('46.41.128.110')
a4 = ipaddress.ip_address('46.41.128.111')
print(a3 > a4)

print('\nwylistowanie sieci')
lista_hostow = ipaddress.ip_network('192.168.2.0/24').hosts()
for host in lista_hostow:
    print(host)
print(lista_hostow)
print(type(lista_hostow))
print(ipaddress.ip_network('192.168.2.0/24'))
print(type(ipaddress.ip_network('192.168.2.0/24')))