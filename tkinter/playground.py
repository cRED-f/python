# *args take all the value as a tuple
def add(*args):
    print(args[0])
    sum = 0
    for i in args:
        sum += i
    print(sum)


add(3, 2, 1, 4, 6, 9, 7, 8)


# **kwargs(keyword arguments) take value as a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    # for (key,value) in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(10, add=3, multiply=5)


class car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = car(make="Nissan", model="GTR")
print(my_car.make)
