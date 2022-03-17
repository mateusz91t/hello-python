import numpy as np
import random
from timeit import timeit


# t = np.arange(10**10)  # error - not enough memory [74 GB RAM] - nice info
t = np.arange(10**9)  # the fastest and cheapest of memory
del t



from algorytmy.func_check_time import (
    check_time_list_read,
    check_time_list_append,
    check_time_array_read
)

timeit("check_time_list_read(20)")
timeit("check_time_list_append(20)")
timeit("check_time_array_read(20)")
