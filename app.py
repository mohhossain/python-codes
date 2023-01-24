class Racoon:

    count = 0

    def __init__(self, name, sex, age, number_of_hot_dogs_eaten=0, hasRabies=False):
        self.name = name
        self.sex = sex
        self.age = age
        self.hasRabies = hasRabies
        self.number_of_hot_dogs_eaten = number_of_hot_dogs_eaten
        Racoon.count += 1

    def print_info(self):
        print(
            f"This is {self.name} and this racoon has eaten {self.number_of_hot_dogs_eaten} hot dogs")

    @classmethod
    def get_count(cls):
        print(cls.count)


rocket_bob = Racoon("Rocket Bob", "M", 3, False, 100)

bandit = Racoon("Bandit", "M", 4, 200, True)

rocket_bob.name = "Rocket"

print(rocket_bob.name)
print(rocket_bob.number_of_hot_dogs_eaten)

print(Racoon.get_count())

bandit.print_info()
