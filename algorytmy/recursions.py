def factorial(num: int) -> int:
    if num > 1:
        return num * factorial(num -1)
    else:
        return 1


factorial(5)


def sum_list_loop(lst: list) -> int:
    result = 0
    for element in lst:
        result += element
    return result


sum_list_loop(list(range(5)))


def sum_list_recursion(lst: list):
    if lst == list():
        return 0
    return lst[0] + sum_list_recursion(lst[1:])


sum_list_recursion(list(range(5)))


def count_list_recursion(lst):
    if not lst:
        return 0
    return 1 + count_list_recursion(lst[1:])


count_list_recursion(list(range(5)))


# def find_max(lst):
#     if not lst:
#         return
#     return
