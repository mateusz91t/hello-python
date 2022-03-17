import string


string.digits
string.ascii_uppercase
string.ascii_letters
string.printable
string.punctuation
string.whitespace
list(string.digits)


from collections import Counter
s1 = 'apppend'
Counter(s1)  # zlicz elementy


import math
math.factorial(5)  # silnia


words = ['This', 'is', 'a', 'list', 'of', 'words', s1]
max(words, key=len)  # longest word


s1.count('p')  # count `p` letter


import time
time.ctime()  # human readable


a, *b, c = [*range(1, 6)]
a, b, c
