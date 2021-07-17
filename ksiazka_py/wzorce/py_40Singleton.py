# Singleton
class Dbc:
    instance = None

    def __new__(cls, *args, **kwargs) -> instance:
        if cls.instance is None:
            print('connecting to database...')
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


c1 = Dbc()
c = Dbc()
print(id(c), id(c1), c is c1, sep='\n')
