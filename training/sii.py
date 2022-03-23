# słownik klucze 0-100 , vals 1-101
d = {x: x+1 for x in range(100)}
d

def palindrom(s):
    return s.lower() == s.lower()[::-1]


print(palindrom('Ala')) #True


