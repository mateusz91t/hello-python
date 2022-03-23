def check_time_list_read(times: int):
    # l = list(range(10**9))  # crash cp!!!
    l = list(range(10**8))
    for i in range(times):
        ri = random.randint(0, len(l))
        l[ri]
    del l


def check_time_list_append(times: int):
    # l = list(range(10**9))  # crash cp!!!
    l = list(range(10**8))
    for i in range(times):
        ri = random.randint(0, len(l))
        l.append(ri)
    del l


def check_time_array_read(times: int):
    # tp = array('i', range(10**9))  # very slow creating but works!
    tp = array("i", range(10**8))  # cheaper and slower creating than lists
    for i in range(times):
        ri = random.randint(0, len(l))
        l[ri]
    del tp
