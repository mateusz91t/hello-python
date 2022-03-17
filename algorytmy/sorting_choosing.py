import random


def find_min(lst: list) -> int:
    min_id = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_id]:
            min_id = i
    return min_id


def sort_choosing(lst: list) -> list:
    lst_copy = lst.copy()
    out_list = list()
    counter = 0
    while lst:
        counter += 1
        out_list.append(lst.pop(find_min(lst)))
    lst = lst_copy
    return counter, out_list


l = list(range(20))
random.shuffle(l)
sort_choosing(l)
