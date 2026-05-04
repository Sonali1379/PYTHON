class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


if __name__ == "__main__":
    animals = [Animal(), Dog(), Cat()]
    for a in animals:
        print(a.speak())
