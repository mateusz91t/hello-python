import re

p1 = r'<(\w+?)\ ??((?<=\ )(.*?)(?=\>))*?>(.+?)<\/(\w+?)>'
# p1 = r'<(\w+)(\ ?\ .*?)?(>)(.+)(</\1>)'
f1 = open('xml1.xml', 'r+')
t1 = f1.readlines()

print(t1)
re1 = re.compile(p1, re.M)
# m1 = re1.match(t1)
# print()
# print(m1)
# print(m1.groups())


outstr = ''

for line in t1:
    m1 = re1.search(line)
    if not m1:
        outstr += line
    else:
        g1 = m1.groups()
        outstr += f'<{g1[0]}>{g1[0]}</{g1[0]}>'

print(outstr)
