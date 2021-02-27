from contextlib import contextmanager


def gen():
    yield 1
    yield 2
    yield 1234


for _ in gen():
    print(_)


def gen2():
    for x in range(10):
        if x % 2:
            yield x

for _ in gen2():
    print(_)


# print(gen2()[2])  # TypeError: 'generator' object is not subscriptable

@contextmanager
def get_file(path: str):
    f = open(path, 'r+')
    try:
        yield f
    finally:
        f.close()


f1 = get_file('../files_sources/airtravel.csv')
print(f1)  # jak z tego skorzystać?

with f1 as ff:
    for line in ff:
        print(line)


class ContMgr:
    def __init__(self, path: str):
        self.name = path
        print('init method')

    def __enter__(self):
        print('enter method')
        self.file = open(self.name, 'r+', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print(f'exit method, exc_type = {exc_type}, exc_val = {exc_val}, exc_tb = {exc_tb}')


# with ContMgr('../files_sources/tekst.txt') as resource:
#     for line in resource:
#         print(line)

