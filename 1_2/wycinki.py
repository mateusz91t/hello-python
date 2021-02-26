# slices - wycinki

list_1: list = list(range(0, 15))
print(list_1)

# sekwencje: a[start:end:step]
print(
    'ostatni element: list_1[-1] =\n',
    list_1[-1]
)
print(
    'sekwencja [od_włącznie - do_wyłącznie): list_1[7:10] =\n',
    'czyli od 7 do 10\n',
    list_1[7:10]
)
print(
    'sekwencja od 0 do ostatnich 2ch el: list_1[:-2] =\n',
    list_1[:-2]
)
print(
    'sekwencja od do 20 ze skokiem 4: list_1[2:20:4] =\n',
    list_1[2:20:4]
)

print(f"{'*' * 100}")
print(f"{'-'.join('*' for _ in range(50))}")

# ::
print(
    'reversed: list_1[::-1] =\n',
    list_1[::-1]
)
print(
    'reversed every 2nd element: list_1[::-2] =\n',
    list_1[::-2]
)