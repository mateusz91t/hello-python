import re
# arg1 to pattern, w którym wyznaczyłem sobie kilka grup;
# w arg2 wymieniam sobie linię, którą znalazłem regexem od < do > tak, aby 1-sza grupa była w nazwie tagu i zawartości
# arg3 to plik w którym zapisuję wynik
with open('../files_sources/xml1.xml', 'r+') as source:
    text_source = source.read()
t1 = re.sub(r'<(\w+)( .*)*>(.+)(</\1>)', r'<\1>\1</\1>', text_source)
with open('../files_sources/xml2.xml', 'w+') as target:
    target.write(t1)

print(t1)
