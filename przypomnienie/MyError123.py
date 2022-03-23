class MyError1(Exception):
    def __init__(self, ex, mess):
        self.mess = mess
        self.ex = ex
        print(ex, mess)

