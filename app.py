from itertools import count


class Car:
    count = 0

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        Car.count += 1

    def __str__(self):
        return f'{self.make}, {self.model}, {self.year}'

    @classmethod
    def instanceCount(cls):
        return cls.count

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


car1 = Car("Toyota", "Camry", 2023, "Red")
print(Car.instanceCount())
print(car1.getColor())
car1.color = "black"
print(car1.getColor())
