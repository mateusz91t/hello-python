class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, val):
        self._x = val

    def delx(self):
        del self._x


c1 = C()
c1._x = 2
print(c1.getx())
c1.setx(4)
print(c1.getx())
c1.delx()


class D:
    def __init__(self):
        self.__y = None

    @property
    def y(self):
        print("@property:")
        return self.__y

    @y.setter
    def y(self, val):
        print("@y.setter:")
        self.__y = val

    @y.deleter
    def y(self):
        print("@y.deleter:")
        del self.__y


print("\nd1:")
d1 = D()
# każde przypisanie uruchomi metodę setter y
d1.y = 2
# a każda próba dostępu uruchomi metodę getter @property
print(d1.y)
