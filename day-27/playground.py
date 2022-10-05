def add(*args):
    # print(args[0])
    answer = 0
    for i in args:
        answer += i
    return answer


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def calculate(n, **kwargs):
    print(kwargs)

    n *= kwargs["multiply"]
    n += kwargs["add"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get("make")
        self.model = kwargs["model"]
        self.seats = kwargs.get("seats")
        self.color = kwargs.get("color")


my_car = Car(model="sonata")
print(my_car.make, my_car.model)
