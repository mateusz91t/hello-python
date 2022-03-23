# internal functions
# funkcje wewnętrzne

def silnia1(silnia_od: int = 10):
    return 1 if silnia_od <= 1 else silnia_od * silnia1(silnia_od - 1)



def silnia2(silnia_od: int = 10):
    def foo(silnia_od):
       return 1 if silnia_od <= 1 else silnia_od * foo(silnia_od - 1)
    return (foo(silnia_od))


print(silnia2(997))
print(silnia1(998))
# print(silnia1(999))  # give an error max recursion

