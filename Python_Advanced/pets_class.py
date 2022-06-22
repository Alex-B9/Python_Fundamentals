# Parent class
class Dog:
    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # instance method
    def eat(self):
        print("it's time to eat")
        self.is_hungry = False

    def walk(self):
        return "{} walk !".format(self.name)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    # def run(self, speed):
    #     return "{} runs {}".format(self.name, speed)

    def __init__(self, name, age):
        super().__init__(name, age)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Parent class
class Pets:
    def __init__(self):
        # instance of dogs
        self.dogs = [
            RussellTerrier("Tom", 6),
            Bulldog("Larry", 7),
            Bulldog("Fletcher", 9)
        ]

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


pets = Pets()
print("I have {} dogs".format(len(pets.dogs)))
print(pets.dogs[0].description() + ",")
print(pets.dogs[1].description() + ",")
print(pets.dogs[2].description())
print("And they're all {}s, of course.".format(pets.dogs[0].species))

# Hungry condition
# if pet.dogs[0].is_hungry and pet.dogs[1].is_hungry and pet.dogs[2].is_hungry:
#     print("My dogs are hungry")
# else:
#     print("My dogs are not hungry")

# hungry = ("My dogs are not hungry", "My dogs are hungry")[
#     pets.dogs[0].is_hungry and pets.dogs[1].is_hungry and pets.dogs[2].is_hungry]
#
# print(hungry)

for pet in pets.dogs:
    if pet.is_hungry:
        pet.eat()

count = 0

for pet in pets.dogs:
    if not pet.is_hungry:
        count += 1

if count == 3:
    print("My dogs it's not hungry")

