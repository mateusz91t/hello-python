def get_data(file):
    with open(file, mode='r') as file_triangle:
        lists_triangle = file_triangle.read().split('\n')
        for i in range(len(lists_triangle)):
            lists_triangle[i] = list(
                int(x)
                for x
                in lists_triangle[i].strip().split()
            )
        del lists_triangle[-1]
        return lists_triangle


def get_all_paths(data_source):
    list_out = list()
    len_path = len(data_source)
    list_out.append([0])
    for x in range(len_path - 1):
        list_out = increase_paths(list_out)
    list_out.sort()
    return list_out


def increase_paths(list_in):
    print(len(list_in[0]))
    list_out = list()
    while list_in:
        cur_list = list_in.pop()
        last_el = cur_list[-1]
        cur_list.append(last_el)
        list_out.append(cur_list)
        cur_list = cur_list.copy()
        cur_list[-1] += 1
        list_out.append(cur_list)
    return list_out


def map_paths(paths: list, data: list) -> list:
    list_out = list()
    while paths:
        cur_path = paths.pop()
        mapped_path = list()
        for x in range(len(cur_path)):
            mapped_path.append(
                data[x][cur_path[x]]
            )
        list_out.append(mapped_path)
    return list_out


def sum_and_sort_mapped_paths(list_mapped_paths: list) -> list:
    list_out = list()
    while list_mapped_paths:
        list_to_sum = list_mapped_paths.pop()
        list_out.append((sum(list_to_sum), list_to_sum))
    list_out.sort(key=lambda tup: tup[0], reverse=True)
    return list_out


def present_results(list_to_present: list):
    for el in list_to_present:
        print(el)


def get_minpath_mincount(file_source):
    data = get_data(file_source)
    paths = get_all_paths(data)
    # print(paths)
    mapped_paths = map_paths(paths, data)
    mapped_paths.reverse()
    # print(mapped_paths)
    summed_and_sorted = sum_and_sort_mapped_paths(mapped_paths)
    present_results(summed_and_sorted)



very_easy = 'D:/Mateusz/nauka/python/python_lvl_up/zad_rekr/1-very_easy.txt'
easy = 'D:/Mateusz/nauka/python/python_lvl_up/zad_rekr/2-easy.txt'
medium = 'D:/Mateusz/nauka/python/python_lvl_up/zad_rekr/3-medium.txt'
# get_minpath_mincount(very_easy)
get_minpath_mincount(easy)
# get_minpath_mincount(medium)
