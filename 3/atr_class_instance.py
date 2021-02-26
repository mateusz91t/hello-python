class Dog:
    dogs_counter = 0
    dogs: list = list()
    _prv_str: str = 'private string!'
    __more_prv_str: str = 'more private string!'

    def __init__(self, name: str, weight: int = 5):
        self.name = name
        self.weight = weight
        self._prv_field = "object's prv field"
        self.__more_prv_field = "object's more prv field"
        Dog.dogs_counter += 1
        Dog.dogs.append(self)

    def prn_dog(self):
        return f"Dog's name is {self.name}, and its weight is {self.weight}"


print('Dog.dogs_counter =', Dog.dogs_counter)
print('Dog.dogs =', Dog.dogs)
dog_1: Dog = Dog('Bonifacy')
print('Dog.dogs_counter =', Dog.dogs_counter)
print('Dog.dogs =', Dog.dogs)
print(dog_1.prn_dog())

Dog.dogs.append('xyz')
print('Dog.dogs =', Dog.dogs)
print('dog_1.dogs =', dog_1.dogs)

dog_1.dogs = list(range(10))
print('Dog.dogs =', Dog.dogs)
print('dog_1.dogs =', dog_1.dogs)

dog_1.a = 'ssed'
print('dog_1.a =', dog_1.a)
print('dog_1._prv_str =', dog_1._prv_str)
# print(dog_1.__more_prv_str)  # doesn't work!

dog_1.__b = 'dess'
print('dog_1.__b =', dog_1.__b)
print('dog_1._prv_field =', dog_1._prv_field)
# print('dog_1.__more_prv_field =', dog_1.__more_prv_field)  # doesn't work!


print(
    '\nDog.__dict__ =\n',
    Dog.__dict__
)
print(
    'dog_1.__dict__ =\n',
    dog_1.__dict__
)

print(
    'vars(dog_1) =\n',
    vars(dog_1)
)
print(
    'vars(Dog) =\n',
    vars(Dog)
)