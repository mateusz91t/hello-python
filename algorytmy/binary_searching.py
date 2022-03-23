def search_for(lst: list, num: int):
    min_id, max_id = 0, len(lst) - 1
    counter = 0
    mid_id = round((min_id + max_id) / 2)
    while max_id - min_id >= 0:
        mid_id = round((min_id + max_id) / 2)
        # print(f'min = {lst[min_id]} \tmid = {lst[mid_id]} \tmax = {lst[max_id]}')
        if lst[mid_id] < num:
            min_id = mid_id + 1
        elif lst[mid_id] > num:
            max_id = mid_id - 1
        else:
            return mid_id
        print(f"min_id = {min_id} \tmid_id = {mid_id} \tmax_id = {max_id}")
        # counter+=1
        # if counter > 10:
        #     break


l = list(range(29))

search_for(l, 19)
