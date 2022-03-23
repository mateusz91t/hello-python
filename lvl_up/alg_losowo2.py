import algorytm_trojkat_silowy as ts
from random import choice, choices
import datetime as dt


# random
def get_next_index1(last_element_index, data_level, data) -> int:
    return last_element_index + choice([0, 1])


# prosty wybór: zwróci ten mniejszy z prawdopodobieństwem większym ile jest mniejszy
def get_next_index2(last_element_index, data_level, data):
    next1, next2 = data[data_level][last_element_index], data[data_level][last_element_index + 1]
    chance1, chance2 = (10-next1) / 10, (10-next2) / 10
    return choices(
        [last_element_index, last_element_index + 1],
        [chance1, chance2]
    )[0]


# todo wysokość: im jest niżej tym większa szansa, że zwróci ten mniejszy
def get_next_index3(last_element_index, data_level, data):
    next1, next2 = data[data_level][last_element_index], data[data_level][last_element_index + 1]
    chance1, chance2 = 1, 1
    data_len = len(data)
    lvl_reduce_worst_chance = 1 - ((data_len - data_level + 1) / data_len)
    if next1 < next2:
        chance2 *= lvl_reduce_worst_chance
    elif next1 > next2:
        chance1 *= lvl_reduce_worst_chance
    return choices(
        [last_element_index, last_element_index + 1],
        [chance1, chance2]
    )[0]


# todo mieszane: tym większa szansa, że zwróci ten mniejszy 1) im jest niżej oraz 2) im jest mniejszy
def get_next_index4(last_element_index, data_level, data):
    next1, next2 = data[data_level][last_element_index], data[data_level][last_element_index + 1]
    chance1, chance2 = (10-next1) / 10, (10-next2) / 10
    data_len = len(data)
    lvl_reduce_worst_chance = (data_len - data_level) / data_len
    if next1 < next2:
        next2 *= lvl_reduce_worst_chance
    elif next1 > next2:
        next1 *= lvl_reduce_worst_chance
    return choices(
        [last_element_index, last_element_index + 1],
        [chance1, chance2]
    )[0]


def get_path(readed_data, which_method):
    data_len = len(readed_data)
    path = [0]
    for lvl in range(1, data_len):
        next_idx = which_method(path[-1], lvl, readed_data)
        path.append(next_idx)
    return path


def run(file, which_method, minutes):
    start = dt.datetime.now()
    stop = start + dt.timedelta(minutes=minutes)
    data = ts.get_data(file)
    print(data)
    best_path = get_path(data, which_method)
    best_mapped_path = ts.map_one_path(best_path, data)
    best_result = sum(best_mapped_path)
    best_paths = [(best_path, best_mapped_path, best_result)]
    print(best_path)
    print(best_mapped_path)
    print(best_result)
    while dt.datetime.now() < stop:
        cur_path = get_path(data, which_method)
        cur_mapped_path = ts.map_one_path(cur_path, data)
        cur_result = sum(cur_mapped_path)
        if cur_result <= best_result:
            if cur_result < best_result:
                best_path, best_mapped_path, best_result =\
                    cur_path, cur_mapped_path, cur_result
                best_paths.clear()
                best_paths.append((best_path, best_mapped_path, best_result))
                print(best_path)
                print(best_mapped_path)
                print(best_result)
                print(dt.datetime.now() - start)
            elif (cur_path, cur_mapped_path, cur_result) not in best_paths:
                best_paths.append((cur_path, cur_mapped_path, cur_result))
    print('best:')
    for p in best_paths:
        print(p[0])
        print(p[1])
        print(p[2])


# run(ts.very_easy, get_next_index1, 1)
# run(ts.easy, get_next_index1, 1)
# run(ts.medium, get_next_index1, 420)
run(ts.medium, get_next_index3, 420)
# [0, 0, 1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 12, 12, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28, 28, 28, 28, 28, 29, 30, 30, 31, 32, 33, 33, 34, 34, 34, 34, 34, 34, 34, 35, 36, 37, 38, 39, 39, 39, 39, 39, 39, 39, 39, 40, 41, 42, 43, 44, 44, 45, 46, 46, 46, 47, 47, 48, 49, 50, 50, 50, 51, 51, 51, 52, 53]
# [5, 4, 3, 2, 1, 1, 7, 1, 2, 1, 3, 6, 3, 2, 1, 1, 1, 4, 1, 1, 6, 4, 3, 3, 3, 1, 8, 2, 3, 1, 7, 9, 3, 4, 1, 1, 4, 1, 2, 3, 2, 1, 6, 1, 2, 1, 5, 8, 2, 4, 5, 1, 5, 2, 2, 1, 6, 2, 3, 4, 5, 4, 3, 2, 3, 3, 1, 3, 3, 2, 1, 6, 1, 3, 3, 6, 1, 1, 3, 3, 2, 5, 4, 9, 2, 5, 3, 3, 4, 2, 2, 1, 1, 6, 9, 1, 1, 1, 5, 8]
# 313
# 5:48:21.995692