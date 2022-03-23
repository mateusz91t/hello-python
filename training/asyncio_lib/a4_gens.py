# a common generator
def count_to(max_value):
    i = 0
    while i <= max_value:
        print('before yield')
        yield i
        print('after yield')
        i += 1


c1 = count_to(3)
next(c1)
c1.send(0)
for el in count_to(2):
    print(el)


# a gen with send methon - to change the state in a gen
# set and back to new value during a generator runs
def count_to_send(max_value):
    i = 0
    while i <= max_value:
        j = (yield i)  # try to set everytime
        if j is not None:  # if not set - increment
            i = j
        else:
            i += 1


c2 = count_to_send(3)
next(c2)
c2.send(0)


# an internal generator
def another_count():
    yield 40


def count_to_internal(max_val):
    i=0
    while i <= max_val:
        yield i
        i += 1
    yield from another_count()


c3 = another_count()
next(c3)

c4 = count_to_internal(3)
next(c4)
for el in c4:
    print(el)
